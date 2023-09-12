# Educational Administration Tracker System (Backend)

## 🌟 Overview
A platform designed to assist educational institutions in managing, tracking, and evaluating the performance of their individual departments. The system not only tracks performance but also provides feedback in the form of scores, remarks, and mechanisms to address highlighted concerns.

## ❗ Problem Definition
Traditional educational administration often relies on manual record-keeping, paper-driven feedback systems, and non-centralized data. This leads to:
- Mismanagement of records.
- Inefficiencies in feedback and performance evaluation.
- Difficulty in monitoring departmental progress and performance.
- Challenges in addressing and tracking resolutions to identified problems.

The Educational Administration Tracker System aims to streamline these processes, offering a centralized, digital solution to manage, evaluate, and improve the performance of individual departments within educational institutions.

## 🛠 Key Features

### ➡️ School Profile Creation
- **Name of the school**: A unique identifier for each school.
- **School Level**: Specify whether the school is primary, secondary, or higher secondary (or any other classification relevant to your region).
- **School ID**: A unique code or number assigned to the school for tracking and identification purposes.
- **Additional details**: Address, principal's name, number of students, faculty, etc.

### ➡️ Departmental Evaluation
- Consists of 14 different departments per school.
- Trackers evaluate each department based on various fields/criteria.
- Score assignment for every department.
- Remark fields for detailed feedback, allowing for binary responses (right/wrong or true/false).

### ➡️ Departmental Administration
- Each department is overseen by its admin.
- Admins can view detailed statistics on their department's performance.
- Ability to respond to feedback/problems highlighted during evaluations.

### ➡️ Problem Resolution Plans
- Formulate plans based on feedback and scores.
- Monitor the progress of these plans.
- Details include objectives, tasks, responsible personnel, deadlines, and status.

### ➡️ Managerial Oversight
- A central manager for an overarching view.
- Views consolidated statistics and reports.
- Reviews and comments on departmental plans.
- Prioritizes and adds objectives for departments.

### ➡️ Dashboard & Reporting
- Graphics for scores, evaluations, and progress.
- Compares departments both within and across schools.
- Managerial dashboard for comprehensive statistics and metrics.

## 💻 Technical Stack

Leveraging a robust technical stack to guarantee top-notch performance and a pleasant user experience:
- **Backend Framework**: Django
- **Database**: AWS PostgreSQL for reliable and scalable data management
- **Storage**: AWS S3 for steadfast and scalable storage of static and media files
- **Email Services**: Integration with SendGrid for reliable email notifications and alerts
- **Image Optimization**: Adoption of webp format for image conversions, enhancing webpage loading time significantly.

## 🛠 Setup and Installation

### Prerequisites

Ensure your system houses the following prerequisites:
- Python (3.9 or higher)
- Django (4.2 or higher)
- PostgreSQL

### Installation

Adhere to the following instructions for a seamless local setup:

```bash
# Clone the repository
git clone https://github.com/zico-son/Digital-Museum.git

# Navigate to the project directory
cd digital-museum-backend

# Set up a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the necessary requisites
pip install -r requirements.txt

# Execute database setups
python manage.py migrate

# Run the server
python manage.py runserver
```

## 🔗 Frontend Repository

For Frontend functionalities, database operations, and other server-side logic related to the Educational Administration Tracker System, please navigate to the [Frontend repository](https://github.com/amatter23/Educational-Administration-Tracker-System/).


## 📢 Feedback & Contributions
Your feedback is invaluable in refining this Backend application. We encourage contributions. Please feel free to open an issue or submit a pull request.


## 📞 Contact
For any queries, suggestions, or collaborative efforts, reach out at [LinkedIn](https://www.linkedin.com/in/a-zakaria-/).
