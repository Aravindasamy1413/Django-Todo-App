# 📝 Django To-Do Web Application

A fully functional and user-friendly **To-Do List Web Application** built using **Django**. This project allows users to manage daily tasks efficiently with features like task creation, completion tracking, notes management, and trash recovery.

---

## 🚀 Features

* ✅ User Authentication (Login & Register)
* 📝 Add, Update, and Delete Tasks
* ✔️ Mark Tasks as Completed
* 🔄 Restore Completed Tasks
* 🗑️ Trash Management (Soft Delete & Restore)
* 📌 Notes Section for additional information
* 🔒 User-specific Data (Each user has their own tasks)
* 🎯 Clean and Professional UI

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS
* **Database:** SQLite3
* **Authentication:** Django Built-in Auth System

---

## 📂 Project Structure

```
todo_project/
│── manage.py
│── db.sqlite3
│── requirements.txt
│
├── todo_app/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── static/
│
└── README.md
```

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/todo-project.git
cd todo-project
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate Virtual Environment

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Apply Migrations

```bash
python manage.py migrate
```

### 6️⃣ Run the Server

```bash
python manage.py runserver
```

### 7️⃣ Open in Browser

```
http://127.0.0.1:8000/
```

---

## 🧪 Testing the Project

Run system checks:

```bash
python manage.py check
```

If it shows:

```
System check identified no issues (0 silenced)
```

✔️ Your project is working correctly.

---

## 🔄 Task Workflow

* Add Task → Stored in Home Page
* Complete Task → Moves to Completed Page
* Delete Task → Moves to Trash
* Restore from Trash → New ID generated
* Restore Completed Task → Same ID retained

---

## ⚠️ Notes

* `db.sqlite3` can be removed before uploading to GitHub.
* Migrations can also be removed, but users must run migrations again.
* Always include `requirements.txt`.

---

## 📌 Future Improvements

* 🌐 Deploy to cloud (Render / AWS / Heroku)
* 🎨 Improve UI with Bootstrap or Tailwind CSS
* 🔔 Add Notifications / Reminders
* 📱 Make Fully Responsive Design

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 👨‍💻 Author

Developed by **Aravindasamy**

---

⭐ If you like this project, don't forget to give it a star on GitHub!


<img width="1918" height="1008" alt="01" src="https://github.com/user-attachments/assets/e48c7d81-fc77-44df-8613-de77757905d6" />

<img width="1918" height="1022" alt="02" src="https://github.com/user-attachments/assets/89a8d57b-7a9f-4a6e-83e9-7fd935911e64" />

<img width="1918" height="1022" alt="03" src="https://github.com/user-attachments/assets/0bbc7e76-5eb7-4a5b-a464-d0eaf2fb9747" />

<img width="1918" height="1021" alt="04" src="https://github.com/user-attachments/assets/4e60dfb7-a7cb-49fb-8920-783301799ef5" />

<img width="1918" height="1017" alt="05" src="https://github.com/user-attachments/assets/18091b96-926b-4d00-8f78-5e4ccccf5368" />

<img width="1918" height="1018" alt="06" src="https://github.com/user-attachments/assets/2c9bc661-2b34-48eb-b9de-54fd64394bd6" />

<img width="1918" height="1022" alt="07" src="https://github.com/user-attachments/assets/6af1f238-c284-4864-b164-98634ae515d6" />

<img width="1918" height="1017" alt="08" src="https://github.com/user-attachments/assets/fd868f6c-d4cc-400c-ad94-8a045a35224c" />

<img width="1918" height="1016" alt="09" src="https://github.com/user-attachments/assets/bce41f80-5ed6-4fd2-8764-ed08cc0100cb" />
