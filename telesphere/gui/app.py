import sys

from telesphere.classes.contact_list import ContactList
from telesphere.classes.contacts import Contact
from telesphere.databases.contact_database import ContactDatabase
from telesphere.database.phone_database import PhoneDatabase

from tkinter import Tk, Frame, Label, Entry, Button, StringVar, IntVar, DoubleVar, messagebox

cache = ContactList()

def submit():
    try:
        new_contact = Contact(uuid.get(), phone_number.get(), email.get()
        
        global cache
        
        cache.append(new_contact)
        
        uuid.set('')
        phone_number.set('')
        email.set('')
        
        messagebox.showinfo("", f'Added {new_contact} to cache!')
    except FakeContactException as e:
        # Add FakeContactException
        messagebox.showerror("!", str(e))        

def search_contacts(uuid: str):
    global cache
    idx = 0
    
    for contact in cache:
        if contact.uuid == uuid:
            return idx
        else:
            idx += 1
            
    return -1
    
def update():
    try:
        uuid = uuid.get()
        new_contact = Contact(uuid, phone_number.get(), email.get()
        
        global cache
        cache_idx = search_contacts(uuid)
        
        if cache_idx == -1:
            messagebox.showerror("!", "Can't find the uuid in cache!")
        else:
            cache[cache_idx] = new_contact
        
            uuid.set('')
            phone_number.set('')
            email.set('')
            
            messagebox.showinfo("", f'Updated {new_contact} in cache!')
    except FakeContactException as e:
        # Add FakeContactException
        messagebox.showerror("!", str(e)) 

def delete():
    try:
        uuid = uuid.get()
        
        global cache
        cache_idx = search_contacts(uuid)
        
        if cache_idx == -1:
            messagebox.showerror("!", "Can't find the uuid in cache!")
        else:
            del cache[cache_idx]
        
            uuid.set('')
            phone_number.set('')
            email.set('')
            
            messagebox.showinfo("", f'Deleted {new_contact} in cache!')
    except Exception as e:
        # Add FakeContactException
        messagebox.showerror("!", str(e)) 

def flush():
    try:
        global cache

        cache.to_database()
        
        messagebox.showinfo("", f'Flushed cache to database!')
    except Exception as e:
        # Add FakeContactException
        messagebox.showerror("!", str(e)) 

def empty():
    global cache 
    
    cache.empty()
    
    messagebox.showinfo("", "Emptied the cache!")

def export():
    try:
        global cache

        cache.to_csv()
        
        messagebox.showinfo("", f'Flushed cache to database!')
    except Exception as e:
        # Add FakeContactException
        messagebox.showerror("!", str(e)) 

if __name__ == "__main__":
    database_location = sys.argv[1]
    
    root = Tk()
    root.title("Telesphere Contact Database - PCPP1")
    root.geometry("600x900")

    uuid = Entry(root, width=30)
    phone_number = Entry(root, width=30)
    email = Entry(root, width=30)

    uuid.grid(row=0, column=1, padx=20, pady=(10,0))
    phone_number.grid(row=1, column=1, padx=20)
    email.grid(row=2, column=1, padx=20)

    uuid_label = Label(root, text="UUID")
    phone_number_label = Label(root, text="Phone Number")
    email_label = Label(root, text="Email")

    uuid_label.grid(row=0, column=0, pady=(10,0))
    phone_number_label.grid(row=1, column=0)
    email_label.grid(row=2, column=0)

    add_btn = Button(root, text="Add Record", command=submit)
    update_btn = Button(root, text="Update Record", command=update)
    delete_btn = Button(root, text="Delete Record", command=delete)

    add_btn.grid(row=4, column=0)
    update_btn.grid(row=4, column=1)
    delete_btn.grid(row=4, column=2)

    cache_frame = Frame()
    cache_frame.grid(row=6, column=0, columnspan=3)

    flush_btn = Button(cache_frame, text="Persist Data", font=("arial", 12, "bold"), command=flush)
    empty_btn = Button(cache_frame, text="Delete Cache", command=empty)
    export_btn = Button(cache_frame, text="Export Data", command=export)

    flush_btn.grid(row=0, column=0)
    empty_btn.grid(row=0, column=1)
    export_btn.grid(row=0, column=2)

    root.mainloop()
