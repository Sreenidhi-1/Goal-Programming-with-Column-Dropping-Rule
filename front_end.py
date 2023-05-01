import tkinter as tk

def display(d,l,sol):
    root = tk.Tk()
    root.title("Simplex Table")
    root.configure(bg="black")
    iteration_num = 0
    for data in d:
        iteration_num += 1
        iteration_label = tk.Label(root, text=f"Final Iteration", font=("Arial", 12, "bold"), pady=5,bg="black", fg="white")
        iteration_label.pack()
        table = tk.Frame(root, bd=1, relief=tk.SOLID)
        table.pack()
        header1 = tk.Label(table, text="Basic Variable", font=("Helvetica", 12, "bold"), padx=10, pady=5, borderwidth=1, relief=tk.SOLID, bg="black", fg="white")
        header1.grid(row=0, column=0, sticky="nsew")
        print(data)
        print(data.values())
        max_elements = max([len(value_list) for value_list in data.values()])
        for i in range(max_elements):
            header = tk.Label(table, text=l[i], font=("Arial", 12, "bold"), padx=10, pady=5, borderwidth=1, relief=tk.SOLID, bg="black", fg="white")
            header.grid(row=0, column=i+1, sticky="nsew")
        row_num = 1
        for key, value_list in data.items():
            row_label = tk.Label(table, text=key, font=("Arial", 10), padx=10, pady=5, borderwidth=1, relief=tk.SOLID, bg="black", fg="white")
            row_label.grid(row=row_num, column=0, sticky="nsew")
            for i, value in enumerate(value_list):
                row_value = tk.Label(table, text=value, font=("Arial", 10), padx=10, pady=5, borderwidth=1, relief=tk.SOLID, bg="black", fg="white")
                row_value.grid(row=row_num, column=i+1, sticky="nsew")
                if row_num % 2 == 0:
                    row_label.configure(bg="black")
                    row_value.configure(bg="black")
            row_num += 1
    last=d[-1]
    k=last.keys()
    l=l[:int(len(l)/2)]
    #print(l)
    #print('z2',':',last['z2'][-1])
    """iteration_label = tk.Label(root, text='z2'+':'+str(last['z2'][-1]), font=("Arial", 12, "bold"), pady=5)
    iteration_label.pack()
    for i in l:
        if i in k:
                iteration_label = tk.Label(root, text=i+':'+str(last[i][-1]), font=("Arial", 12, "bold"), pady=5)
                iteration_label.pack()
        else:
                iteration_label = tk.Label(root, text=i+':'+str(0), font=("Arial", 12, "bold"), pady=5)
                iteration_label.pack()"""
    for x, y in sol.items():
        iteration_label = tk.Label(root, text=x+' : '+str(y), font=("Arial", 12, "bold"), pady=5, bg="black", fg="white")
        iteration_label.pack()
    root.mainloop()
#data1 = {'z': [0.5, 0.0, -2.0, 0.0, -0.75, 0.0, -9.0], 's1': [2.5, 0.0, 2.0, 1.0, 0.25, 0.0, 10.0], 'x3': [-0.5, 1.0, 0.0, 0.0, 0.25, 0.0, 3.0], 's3': [-2.5, 0.0, 8.0, 0.0, -0.75, 1.0, 1.0]}
#data2 = {'z': [0.5, 0.0, -2.0, 0.0, -0.75, 0.0, -9.0], 's1': [2.5, 0.0, 2.0, 1.0, 0.25, 0.0, 10.0], 'x3': [-0.5, 1.0, 0.0, 0.0, 0.25, 0.0, 3.0], 's3': [-2.5, 0.0, 8.0, 0.0, -0.75, 1.0, 1.0]}
#l=['x1','x2','x3','s1','s2','s3','Solution']
#d=[data1]
#display(d,l)