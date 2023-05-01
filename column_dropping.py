import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton
import code
import numpy as np
import math
import copy
import simplyfy
from PyQt5.QtCore import Qt
class LinearProgramming(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Linear Programming Solver')
        self.init_ui()

    def init_ui(self):
        # Create input widgets
        self.objective1_label = QLabel('Objective Function 1:')
        self.objective1_input = QLineEdit()
        self.priority1_label = QLabel('Priority :')
        self.priority1_input = QLineEdit()
        self.objective2_label = QLabel('Objective Function 2:')
        self.objective2_input = QLineEdit()
        self.priority2_label = QLabel('Priority :')
        self.priority2_input = QLineEdit()
        self.condition_label = QLabel('Maximization (1) or Minimization (0):')
        self.condition_input = QLineEdit()
        self.condition2_label = QLabel('Maximization (1) or Minimization (0):')
        self.condition2_input = QLineEdit()
        self.num_constraints_label = QLabel('Number of Constraints:')
        self.num_constraints_input = QLineEdit()
        self.num_constraints_input.textChanged.connect(self.update_constraints)

        self.constraint_labels = []
        self.constraint_inputs = []
        self.right_side_const_labels = []
        self.right_side_const_inputs = []
        self.constraint_vboxes = []

        self.solve_button = QPushButton('Solve')
        self.clear_button = QPushButton('Clear')

        # Create layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.objective1_label)
        vbox.addWidget(self.objective1_input)
        hbox = QHBoxLayout()
        hbox.addWidget(self.priority1_label)
        hbox.addWidget(self.priority1_input)
        hbox.addWidget(self.condition_label)
        hbox.addWidget(self.condition_input)
        vbox.addLayout(hbox)
        vbox.addWidget(self.objective2_label)
        vbox.addWidget(self.objective2_input)
        hbox = QHBoxLayout()
        hbox.addWidget(self.priority2_label)
        hbox.addWidget(self.priority2_input)
        hbox.addStretch()
        hbox.addWidget(self.condition2_label)
        hbox.addWidget(self.condition2_input)
        vbox.addLayout(hbox)

        vbox.addWidget(self.num_constraints_label)
        vbox.addWidget(self.num_constraints_input)

        self.constraint_layout = QVBoxLayout()
        vbox.addLayout(self.constraint_layout)

        hbox = QHBoxLayout()
        hbox.addWidget(self.solve_button)
        hbox.addWidget(self.clear_button)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        palette = self.palette()
        palette.setColor(self.backgroundRole(), Qt.black)
        palette.setColor(self.foregroundRole(), Qt.white)
        self.setPalette(palette)

        # Connect buttons to functions
        self.solve_button.clicked.connect(self.solve)
        self.clear_button.clicked.connect(self.clear)

    def update_constraints(self):
        # Update the number of constraint fields based on the user input
        num_constraints = int(self.num_constraints_input.text())

        # Remove any previously created constraint fields
        for vbox in self.constraint_vboxes:
            self.constraint_layout.removeItem(vbox)
            vbox.deleteLater()

        self.constraint_labels = []
        self.constraint_inputs = []
        self.right_side_const_labels = []
        self.right_side_const_inputs = []
        self.constraint_vboxes = []

        # Create the new constraint fields
        for i in range(num_constraints):
            constraint_label = QLabel(f'Constraint {i+1}:')
            constraint_input = QLineEdit()
            self.constraint_labels.append(constraint_label)
            self.constraint_inputs.append(constraint_input)

            right_side_const_label = QLabel(f'Right Side of Constraint {i+1}:')
            right_side_const_input = QLineEdit()
            self.right_side_const_labels.append(right_side_const_label)
            self.right_side_const_inputs.append(right_side_const_input)

            constraint_vbox = QVBoxLayout()
            constraint_vbox.addWidget(constraint_label)
            constraint_vbox.addWidget(constraint_input)
            constraint_vbox.addWidget(right_side_const_label)
            constraint_vbox.addWidget(right_side_const_input)

            self.constraint_vboxes.append(constraint_vbox)
            self.constraint_layout.addLayout(constraint_vbox)
   

    def solve(self):
    # Get input values
        PRIORITY=[]
        C=[]
        l=[]
        l1=[]
        objective1 = self.objective1_input.text()
        priority1 = self.priority1_input.text()
        condition1 = self.condition_input.text()
        PRIORITY.append(int(priority1))
        C.append(int(condition1))
        l.append(objective1)
        objective2 = self.objective2_input.text()
        priority2 = self.priority2_input.text()
        condition2 = self.condition2_input.text()
        PRIORITY.append(int(priority2))
        C.append(int(condition2))
        l.append(objective2)
        num_constraints = int(self.num_constraints_input.text())
        Constraint_No=num_constraints
        # Get the constraint values
        constraints = []
        right_side_values = []
        for i in range(num_constraints):
            constraint = self.constraint_inputs[i].text()
            right_side = self.right_side_const_inputs[i].text()
            constraints.append(constraint)
            right_side_values.append(int(right_side))
        #INPUT
        def equation_token(lst):
            x=""
            l2=[]
            function_list=[]
            for i in lst:
                j=0
                l2=[]
                while(j<len(i)):
                    while(i[j].isnumeric() or i[j]=='-'):
                        x=x+i[j]
                        if(j!=len(i)-1):
                            j=j+1
                        else:
                            break
                    if(x!=""):
                        l2.append(int(x))
                    x=""
                    j=j+1
                function_list.append(l2)
            return function_list

        lists=equation_token(l)
        objective_function_list=[]
        val=1
        condition=[]
        for i in range(2):
            if(val in PRIORITY):
                objective_function_list.append(lists[PRIORITY.index(val)])
                condition.append(C[PRIORITY.index(val)])
                val+=1
        objective_function_list=(np.array(objective_function_list)*(-1)).tolist()
        no_of_variables=len(objective_function_list[0])
        const_condition=[]
        right_side_const=right_side_values
        constraint_function_list=equation_token(constraints)
        print("cfl", constraint_function_list)
        for i in range (2):
            for j in range(Constraint_No):
                objective_function_list[i].append(0)
        for i in range(Constraint_No):
            const_condition.append(1)

        dial=np.diag([i for i in (const_condition)]).tolist()

        for i in range (Constraint_No):
            constraint_function_list[i]=constraint_function_list[i]+dial[i]
         
        print("OBJECTIVE FUNCTION : " , objective_function_list)      
        print("CONSTRAINT FUNCTION : ",constraint_function_list)  
        print("FUNCTION VALUE OF CONSTRAINT : ",right_side_const)
        print('Condition ; ',condition)
               
               
        #-------------------------------------------------------------------------------------------------------
        #-------------------------------------------------------------------------------------------------------
        #--------------------------------------------INPUT OVER-------------------------------------------------
        #-------------------------------------------------------------------------------------------------------
        #-------------------------------------------------------------------------------------------------------

        def irration(l,dic,l4,condn):
            if(condn==1):
                minimum=0
                for i in range(len(l[0])-1):
                    if(l[0][i]<minimum):
                        minimum=l[0][i]
                z=l[0].index(minimum)
            elif(condn==0):
                maximum=-100000
                for i in range(len(l[0])-1):
                    if(l[0][i]>maximum):
                        maximum=l[0][i]
                z=l[0].index(maximum)
            length=len(l[0])
            ratio=[]
            for i in l:
                if(i[z]!=0 and i[z]>0):
                    ratio.append(i[length-1]/i[z])        
                else:
                    ratio.append(100000000)
            z1=min(ratio)
            pivot_column_index=z
            pivot_row_index=ratio.index(z1)
            pivot_row=l[pivot_row_index]
            pivot=l[pivot_row_index][pivot_column_index]
            new_pivot_row=[]
            for i in pivot_row:
                new_pivot_row.append(i/pivot)
            new_table=[]
            for i in range(len(l)):
                temp=[]
                for j in range(len(l[0])):
                    if(i!=pivot_row_index):
                        temp.append(l[i][j]-l[i][pivot_column_index]*new_pivot_row[j])
                    else:
                        temp.append(new_pivot_row[j])
                new_table.append(temp)
            d={}
            d1=list(dic)
            for i in range(len(new_table)):                    
                if i==pivot_row_index:
                  #print(d[pivot_column_index])
                  d[l4[pivot_column_index]]=new_table[i]  
                else:
                    d[d1[i]]=new_table[i]
            return d
                   


        def min_max(total_list,map,variables,condition):
            if(condition==1):
                m=0
                for i in range(len(total_list[0])-1):
                    if(total_list[0][i]<m):
                        m=total_list[0][i]                               #maximum
                c=1
                while((m<0) and (m!=0)):
                    print("Iteration ",c,":")
                    d2=irration(total_list,map,variables,condition)
                    l2=list(d2.values())
                    for i in l2:
                        print(i)
                    m=0
                    for i in range(len(l2[0])-1):
                        if(l2[0][i]<m):
                            m=l2[0][i]
                    map=d2
                    total_list=l2
                    condition=condition
                    c=c+1
                return map
            elif(condition==0):
                x=[]
                m=-100000                             #minimumization
                for i in range(len(total_list[0])-1):
                    if(total_list[0][i]>m):
                        m=total_list[0][i]
                c=1
                while(m>0):
                    x.append(m)
                    print(x)
                    print("Iteration ",c,":")
                    d2=irration(total_list,map,variables,condition)
                    print(d2)
                    l2=list(d2.values())
                    for i in l2:
                        print(i)
                    m=-100000                              
                    for i in range(len(l2[0])-1):
                        if(l2[0][i]>m):
                            m=l2[0][i]
                    map=d2
                    total_list=l2
                    condition=condition
                    c=c+1
                return map

        for i in range(len(constraint_function_list)):
            constraint_function_list[i].append(right_side_const[i])
        for i in range(len(objective_function_list)):
            objective_function_list[i].append(0)
        total_list=objective_function_list+constraint_function_list



        map={}
        for i in range(len(total_list)):
            if(i<2):
                map['z'+str(i+1)]=total_list[i]
            elif(i>=2):
                map['s'+str(i+1-2)]=total_list[i]


        

        def column_dropping(simplex_table,i,var,iteration):
            keys=list(simplex_table.keys())
            solutions[keys[0]]=simplex_table[keys[0]][-1]
            col_index=[]
            for j in range(len(simplex_table[keys[i]])-1):
                if(simplex_table[keys[i]][j]!=0):
                    col_index.append(j)
                    if(i==0):
                        del var[j]
            col_index.sort(reverse=True)
            del simplex_table[keys[i]]
            keys=list(simplex_table.keys())
            for i in range(len(simplex_table)):
                for j in col_index:
                    del simplex_table[keys[i]][j]
            #print(simplex_table)
            map=simplex_table
            var=list(simplex_table.keys())
            total_list=[]
            for i in range(len(simplex_table)):
                total_list.append(simplex_table[var[i]])
            #print('map: ',map)
            #print('total list : ',total_list)
            print('variables : ',variables)
            return simplex_table,total_list,map,variables

        variables=[]
        var=[]
        for i in range(no_of_variables):
            variables.append('x'+str(i+1))
        for i in range(len(constraint_function_list)):
            variables.append('s'+str(i+1))
        var=variables
        var.append('Solution')        

        solutions={}
        for i in range(2):
            simplex_table=min_max(total_list,map,variables,condition[i])
            #print("Simplex table : ",simplex_table)
            z={}
            if(len(z)==0):
                z=copy.deepcopy(simplex_table)
            
            final_table,total_list,map,variables=column_dropping(simplex_table,i,var,i)
        simp=[z]
        #print(simp)
        
        #print('Simplex Final : ',z)          
        k=list(z.keys())                    
        for i in range(1,len(z)):            
            solutions[k[i]]=z[k[i]][-1]      
        print('Solutions : ',solutions)  
        simplyfy.display(simp,var,solutions)
       

    def clear(self):
        # Clear all input fields
        self.objective_input.clear()
        self.priority_input.clear()
        self.condition_input.clear()
        self.num_constraints_input.clear()
   
        for constraint_input in self.constraint_inputs:
            constraint_input.clear()
   
        for right_side_const_input in self.right_side_const_inputs:
            right_side_const_input.clear()
    
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    lp = LinearProgramming()
    lp.show()
    sys.exit(app.exec_())

