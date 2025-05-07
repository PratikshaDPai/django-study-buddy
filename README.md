# 📚 Study Buddy

## 📝 Background

Have you ever been part of a study group that fizzled out because people forgot meeting times, lost track of discussions, or didn’t have a space to talk outside of sessions? Study Buddy aims to fix that. It's a minimal yet functional space to post messages inside subject-based groups, organized around common interests (e.g., Python, Algebra, etc.).

---
**Study Buddy** is a lightweight Django web app that lets users create and manage virtual study groups. Within each study group, authenticated users can leave messages—like group announcements, questions, or answers—making it easy to collaborate asynchronously.
![Login Large Screen](https://github.com/user-attachments/assets/1a6436fb-62ef-46be-868c-e52ab892ca63)
![Groups Large Screen](https://github.com/user-attachments/assets/5084684d-1247-45f5-a0af-498f6c75d657)
![Message Large Screen](https://github.com/user-attachments/assets/a1a358fd-7e9c-42e2-8403-cadf1d09c9e2)
![Mobile Responsiveness](https://github.com/user-attachments/assets/1bc8fa9e-f637-40aa-b8f6-e13e011c85fe)

---
## 🌐 Live App

🔗 [View the deployed app on Heroku](https://your-heroku-link-here.com)

---

## 🚀 Getting Started

To run the app locally:

1. Clone the repo:
   ```bash
   git clone https://github.com/PratikshaDPai/django-study-buddy.git
   cd django-study-buddy
   ```

2. Install dependencies using Pipenv:

   ```bash
   pipenv install
   pipenv shell
   ```

3. Create a PostgreSQL database and add credentials in `studybuddy/settings.py`.

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the server:

   ```bash
   python manage.py runserver
   ```

---

## 🔐 Authentication

Study Buddy uses Django’s built-in session-based authentication. Only registered users can create or manage study groups or messages. Guest users can view existing groups but cannot interact beyond that.

---

## 🔧 Technologies Used

* Python 3
* Django
* PostgreSQL
* HTML + CSS (Bootstrap-based layout)
* Heroku (for deployment)

---

## 📁 Features

* **Sign Up / Log In / Log Out** using Django's auth system
* **Create/Edit/Delete Study Groups**
* **Post Messages** within a study group
* **Restrict Edit/Delete to Owners Only**
* Styled UI with consistent purple theme and mobile responsiveness
* WCAG 2.0 AA–compliant color contrasts
* All images have descriptive `alt` text
* All forms are pre-filled on edit

---

## 📌 Planning Materials

* [Study Buddy Project Proposal (PDF)](./studybuddy-proposal%20%282%29.pdf)

---

## 🤝 Attributions

* Study group icon: [Flaticon – Freepik](https://www.flaticon.com/authors/freepik)
* Color palette inspiration: [Coolors.co](https://coolors.co/)

---

## 🔮 Next Steps

* Add the ability to upload files/resources to study groups
* Implement rich text or Markdown support in messages
* Add email notifications for new messages in subscribed groups
* Enable group join requests with admin approval
* Filter groups by topic or tags

---

## 💬 Questions?

Feel free to open an issue or reach out on GitHub!
