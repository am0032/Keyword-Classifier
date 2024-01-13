
import tkinter.font as font
import threading

import tkinter as tk
from tkinter import ttk


# UI
root = tk.Tk()
noise_value=0


import tkinter as tk
import sys


def write_to_text_widget(text_widget, text):
    text_widget.config(state=tk.NORMAL)  # Enable editing
    text_widget.insert(tk.END, text)     # Insert the text
    text_widget.config(state=tk.DISABLED)  # Disable editing to make it read-only
    text_widget.see(tk.END)  # Scroll to the end of the Text widget

# Redirect stdout and stderr to the Text widget
sys.stdout.write = lambda text: write_to_text_widget(output_text, text)
sys.stderr.write = lambda text: write_to_text_widget(output_text, text)




def update_status1(status):
    status_label.config(text=status)

notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, columnspan=1, padx=0, pady=0, sticky="nsew")

# Create a custom style for the notebook to set the background color
notebook_style = ttk.Style()
notebook_style.theme_use('default')
notebook_style.configure('TNotebook.Tab', background='#419292', foreground='black', font=('Helvetica', 10, 'bold'))

# tab for the first program
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Classification Tasks")

#tab for the second program
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="tab2")

#tab for the 3rd program
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="About")




#background color of the widgets within each frame
tab1.configure(style='Custom.TFrame')
tab2.configure(style='Custom.TFrame')
tab3.configure(style='Custom.TFrame')

# Create a custom style for the frames to set the background color
frame_style = ttk.Style()
frame_style.theme_use('default')  # You can use any available theme
frame_style.configure('Custom.TFrame', background='#34495E')


# Configure row and column weights to make the notebook and its contents expand
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


# the label to explain how the program works 
explanation_label = tk.Label(tab1, text="This tab is used to classify excel data for SEO analysis")
explanation_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10, sticky="nsew")
explanation_label.config(bg="#34495E", fg="#8c9da9", font=font.Font(family="Lato", size=9, weight="bold"))

# Create a list of options for the drop-down menu (content for Program 1)
options1 = ["Informative-Noninformative","LSI","Long Tail-Short Tail"]

# Create a StringVar to store the selected option 
selected_option1 = tk.StringVar()

# Set the initial value of the selected option to the first item in the options list 
selected_option1.set(options1[0])

# Create the drop-down menu 
drop_down_menu = tk.OptionMenu(tab1, selected_option1, *options1)
drop_down_menu.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
drop_down_menu.config(bg="#2E4053", fg="#8c9da9", font=font.Font(family="Lato", size=9, weight="bold"))



def set_file_path():
    global user_file_path
    user_file_path = file_path_entry.get().rstrip("\\")



# Create a label and entry widget for file path input
file_path_label = tk.Label(tab1, text="Enter File Path of Model:")
file_path_label.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
file_path_label.config(bg="#34495E", fg="#8c9da9", font=font.Font(family="Lato", size=9, weight="bold"))

file_path_entry = tk.Entry(tab1)
file_path_entry.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

# Create a button to set the file path
set_file_path_button = tk.Button(tab1, text="Set File Path", command=set_file_path)
set_file_path_button.grid(row=3, column=0, columnspan=2, padx=20, pady=5, sticky="nsew")
set_file_path_button.config(bg="#2E778C", fg="black", font=font.Font(family="Lato", size=9, weight="bold"))






def generate_graphs():

 
    if case == 1:
        status_label.config(text="Status: running")  # Update the status label when the task is complete
        
        import pandas as pd
        import numpy as np
        import tkinter as tk
        from tkinter import filedialog
        from tensorflow.keras.models import load_model
        from tensorflow.keras.preprocessing.sequence import pad_sequences
        import pickle
        import os
        status_label.config(text="Status: running")
        
        # Load data using tkinter file dialog
        root = tk.Tk()
        root.withdraw()

        # Select Excel file
        file_path = filedialog.askopenfilename(title="Select Excel file")
        data = pd.read_excel(file_path)
        X = data.iloc[:, 0].values

        # Convert X to lowercase (if needed)
        X = [str(text).lower() for text in X]

        # Select the initial training data folder using tkinter file dialog
        initial_training_data_folder = filedialog.askdirectory(title="Select model and tokenizer folder")

        # Load trained model from the initial training data folder
        model = load_model(os.path.join(initial_training_data_folder, 'trained_model.h5'))

        # Load Tokenizer from the initial training data folder
        tokenizer_path = os.path.join(initial_training_data_folder, 'tokenizer.pkl')
        with open(tokenizer_path, 'rb') as tokenizer_file:
            tokenizer = pickle.load(tokenizer_file)

        # Preprocess the data using the same input_length as in training
        X = tokenizer.texts_to_sequences(X)
        input_length = max(len(sequence) for sequence in X)
        X = pad_sequences(X, maxlen=12)

        # Make predictions
        predictions = model.predict(X)

        # Convert predictions to class labels
        predicted_classes = np.argmax(predictions, axis=1)

        # Add predicted classes to the dataframe
        data['Predicted Classes'] = predicted_classes

        # Save the dataframe back to the Excel file
        data.to_excel(file_path, index=False, header=False)  

        print("Files have been classified")
        status_label.config(text="Status: Completed")

        
   

        
   
           

    if case == 4:
        status_label.config(text="Status: running")  # Update the status label when the task is complete
        
        import pandas as pd
        import numpy as np
        import tkinter as tk
        from tkinter import filedialog
        from tensorflow.keras.models import load_model
        from tensorflow.keras.preprocessing.sequence import pad_sequences
        import pickle
        import os
        # Load data using tkinter file dialog
        root = tk.Tk()
        root.withdraw()

        # Select Excel file
        file_path = filedialog.askopenfilename(title="Select Excel file")
        data = pd.read_excel(file_path)
        X = data.iloc[:, 0].values



        # Load trained model from the initial training data folder
        model = load_model(os.path.join(user_file_path, 'trained_model.h5'))

        # Load Tokenizer from the initial training data folder
        tokenizer_path = os.path.join(user_file_path, 'tokenizer.pkl')
        with open(tokenizer_path, 'rb') as tokenizer_file:
            tokenizer = pickle.load(tokenizer_file)

        # Preprocess the data
        X = tokenizer.texts_to_sequences(X)
        input_length = max(len(sequence) for sequence in X)
        X = pad_sequences(X, maxlen=input_length)

        # Make predictions
        predictions = model.predict(X)

        # Convert predictions to class labels
        predicted_classes = np.argmax(predictions, axis=1)

        # Add predicted classes to the dataframe
        data['Predicted Classes'] = predicted_classes

        # Save the dataframe back to the Excel file
        data.to_excel(file_path, index=False)


        print("Files have been classified")


        status_label.config(text="Status: Completed")  # Update the status label when the task is complete

        
            
        

    elif case==7:

        print("Files have been classified")
        status_label.config(text="Status: Completed")  # Update the status label when the task is complete
            
            
    elif case == 8:
        

        print("Files have been classified")
        status_label.config(text="Status: Completed")  # Update the status label when the task is complete
  
    elif case == 9:
        

        print("Files have been classified")
        status_label.config(text="Status: Completed")  # Update the status label when the task is complete
            
            







############################################


options1 = ["Informative-Noninformative","LSI","Long Tail-Short Tail"]


def set_variables():
    global case
    selected_value1 = selected_option1.get()
  
   
    if selected_value1 == "Informative-Noninformative":
        case = 1
    elif selected_value1 == "LSI":
        case = 2
    elif selected_value1 == "Long Tail-Short Tail":
        case = 3


    
    
    # Start a new thread 
    t = threading.Thread(target=generate_graphs)
    t.start()
    

    


    
root.configure(background="#1e1f26")
# Set the title of the window
root.title("Unravelling Temportal Patterns")





# Create a Text widget for displaying console output in tab1
output_text = tk.Text(tab1, wrap=tk.WORD, bg='#5D6D7E', fg='white',width=70, height=20)  # Set background to black and foreground (text) to white
output_text.grid(row=15, column=1, padx=3, pady=4)

output_label = tk.Label(tab1, text="Console Window:")
output_label.grid(row=15, column=0, columnspan=1, padx=5, pady=5, sticky="nsew")
output_label.config(bg="#34495E", fg="#8c9da9", font=font.Font(family="Lato", size=9, weight="bold"))




button = tk.Button(tab1, text="Perform Classification", command=set_variables, width=20)
button.grid(row=10, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")
button.config(bg="#2E778C", fg="black", font=font.Font(family="Lato", size=9, weight="bold"))

# Create a label to display the status
status_label = tk.Label(tab1, text="Status: Idle")
status_label.grid(row=12, column=0, columnspan=1, padx=5, pady=5, sticky="nsew")
status_label.config(bg="#34495E", fg="black", font=font.Font(family="Lato", size=9, weight="bold"))

# Create a button to stop the program 
stop_button = tk.Button(tab1, text="Stop Program", command=root.destroy)
stop_button.grid(row=12, column=1, columnspan=1, padx=3, pady=4, sticky="nsew")
stop_button.config(bg="#AD2929", fg="white", font=font.Font(family="Lato", size=9, weight="bold"))

root.protocol("WM_DELETE_WINDOW", root.destroy)




label_text = """

A keyword classifier for SEO analysis using machine learning and deep learning methods.
The goal is to reduce work time considerably (within seconds) on classifying keywords into different classes like: Informative, Non-informative, etc

The current best classification accuracy achieved is 91 percent using the deep learning model.

Original Project idea from SCorina.

"""


labelabout = tk.Label(tab3, text=label_text, justify="left")
labelabout.grid(column=0, row=0)
labelabout.grid(row=15, column=0, columnspan=1, padx=5, pady=5, sticky="nsew")
labelabout.config(bg="#5D6D7E", fg="#8c9da9", font=font.Font(family="Lato", size=12, weight="bold"))

root.mainloop()

