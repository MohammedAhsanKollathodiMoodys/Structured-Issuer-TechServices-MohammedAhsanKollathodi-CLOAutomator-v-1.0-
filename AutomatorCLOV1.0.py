# Automated CLO Monitoring 
# CLOAutomator v1.0 is designed to automate CLO monitoring, with basic functionalities and key information integrated into a monitoring and control panel.



import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QTableWidget, QHeaderView, QComboBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class CLOPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CLO Control and Monitoring Panel")
        self.setGeometry(100, 100, 1300, 600)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)

        # Title
        title = QLabel("CLO Control and Monitoring Panel")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Arial", 18, QFont.Bold))
        layout.addWidget(title)

        # Table
        self.table = QTableWidget(6, 9)
        self.table.setHorizontalHeaderLabels([
            "Cluster name", "Schedule", "EMR Status", "Rerun Cluster",
            "Rerun Jenkins Job", "Check S3 File Status", "Activity Monitor Status",
            "Diagnose error / Identified issues", "Revert"
        ])
        clusters = ['A', 'B', 'C', 'D', 'E', 'F']
        for row, cluster in enumerate(clusters):
            # Editable Cluster Name
            cluster_input = QLineEdit(f"Cluster {cluster}")
            cluster_input.setPlaceholderText("Enter cluster name")
            self.table.setCellWidget(row, 0, cluster_input)

            # Editable numeric entry for Schedule
            schedule_input = QLineEdit()
            schedule_input.setPlaceholderText("Enter value")
            self.table.setCellWidget(row, 1, schedule_input)

            # Dropdown for EMR Status
            emr_status = QComboBox()
            emr_status.addItems(["Success", "Failed"])
            self.table.setCellWidget(row, 2, emr_status)

            # Dropdown for Rerun Cluster
            rerun_cluster = QComboBox()
            rerun_cluster.addItems(["Yes", "No"])
            self.table.setCellWidget(row, 3, rerun_cluster)

            # Dropdown for Rerun Jenkins Job
            rerun_jenkins = QComboBox()
            rerun_jenkins.addItems(["Yes", "No"])
            self.table.setCellWidget(row, 4, rerun_jenkins)

            # Button for Check S3 File Status
            s3_button = QPushButton("Check")
            s3_button.setStyleSheet("background-color: #2196F3; color: white; padding: 5px;")
            self.table.setCellWidget(row, 5, s3_button)

            # Dropdown for Activity Monitor Status
            activity_status = QComboBox()
            activity_status.addItems(["Success", "Fail"])
            self.table.setCellWidget(row, 6, activity_status)

            # Text entry for Diagnose error / Identified issues
            error_input = QLineEdit()
            error_input.setPlaceholderText("Enter issue description")
            self.table.setCellWidget(row, 7, error_input)

            # Revert button
            revert_btn = QPushButton("Revert")
            revert_btn.setStyleSheet("background-color: #f44336; color: white; padding: 5px;")
            self.table.setCellWidget(row, 8, revert_btn)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.table)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CLOPanel()
    window.show()
    sys.exit(app.exec_())
