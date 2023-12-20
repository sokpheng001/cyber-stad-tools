from pathlib import Path
from fpdf import FPDF
from datetime import datetime
import matplotlib.pyplot as plt

# Get the current local date and time
current_date_time = datetime.now()

# Format the date as day, month, and year
formatted_date = current_date_time.strftime("%d %B %Y - %H:%M:%S %p")

pdf0 = FPDF()

mitigate_sql_injection = """Preventing injection requires keeping data separate from commands and queries:\n 
1. The preferred option is to use a safe API, which avoids using the interpreter entirely, 
provides a parameterized interface, or migrates to Object Relational Mapping Tools (ORMs). 
[+] Note: Even when parameterized, stored procedures can still introduce SQL injection if 
PL/SQL or T-SQL concatenates queries and data or executes hostile data with EXECUTE 
IMMEDIATE or exec().
2. Use positive server-side input validation. This is not a complete defense as many applications require special 
characters, such as text areas or APIs for mobile applications.
3. For any residual dynamic queries, escape special characters using the specific escape syntax for that interpreter. 
[+] Note: SQL structures such as table names, column names, and so on cannot be escaped, and thus user-supplied 
structure names are dangerous. This is a common issue in report-writing software.
4. Use LIMIT and other SQL controls within queries to prevent mass disclosure of records in case of SQL injection."""


def generate_pie_chart(data, labels, colors):
    # Create a pie chart using matplotlib
    plt.pie(data, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.title("Severity Pie Chart")

    # Save the pie chart as an image
    image_path = 'pie_chart.png'
    plt.savefig(image_path, format='png')
    plt.close()
    return image_path


def generate_bar_chart_image(categories, values, colors):
    plt.bar(categories, values, color=colors)
    plt.xlabel('Severity')
    plt.ylabel('Number of vulnerabilities')
    plt.title('Severity Bar Chart')
    output_path = "bar.png"
    # Save the bar chart as an image
    plt.savefig(output_path, format='png')
    plt.close()
    return output_path


def customer_contact_detail(pdf=pdf0):
    # Add content below the centered image
    pdf.set_y(40)  # Adjust the y-coordinate as needed
    pdf.set_font('Arial', 'B', 25)
    pdf.cell(0, 10, 'Pen-testing report', 0, 1, 'C')
    # Customer details
    # Define the table headers and data
    pdf.set_y(75)  # Adjust the y-coordinate as needed
    headers = ["From Pen-tester", "To Target"]
    data = [
        ["""
                        [CSTAD]
                        """, "Foodie shop"]
    ]

    # Calculate column widths based on available width
    available_width = pdf.w - pdf.l_margin - pdf.r_margin
    col_widths = [available_width / len(headers)] * len(headers)

    # Add table headers
    pdf.set_font("Arial", "B", 12)
    pdf.set_text_color(255, 0, 0)  # Red color
    for header, width in zip(headers, col_widths):
        pdf.cell(width, 10, header, border=1, align="C")
        # pdf.multi_cell(0, 10, '562 Boeng Kork I,\nToul Kok,\nPhnom Penh',border=1)
    pdf.ln()

    # Add table data
    pdf.set_font("Arial", "", 10)
    pdf.set_text_color(0, 0, 0)  # Reset color
    for row in data:
        for cell, width in zip(row, col_widths):
            pdf.cell(width, 10, cell, border=1, align="C")
        pdf.ln()
    # Set font for the Table of Contents

    # pdf.add_page()

    pdf.ln(5)
    #
    pdf.set_left_margin(20)
    pdf.set_right_margin(20)


def content_table(pdf=pdf0):
    pdf.set_font("Arial", "B", 12)
    pdf.set_text_color(255, 0, 0)  # Red color

    # Add "Table of Contents" text
    pdf.cell(0, 10, "Table of Contents", ln=1)

    # Reset font to default
    pdf.set_font("Arial", "", 10)
    pdf.set_text_color(0, 0, 0)  # Reset color

    # Add the content for Table of Contents
    toc_content = [
        "Executive Summary "
        ".............................................................................."
        "................................................. 3",
        "1 Engagement "
        "Summary..................................................."
        "....................................................... 4",
        "1.1 "
        "Scope..........................................................."
        "............................................................................... 4",
        "1.2 Risk "
        "Ratings"
        "................................................................."
        "................................................................... 4",
        "1.3 Findings "
        "Overview"
        "....................................................."
        "............................................................................. 5",
        "2 Technical "
        "Details"
        "......................................................"
        ""
        "............................................................................. 6",
        "2.1 SQL Injection "
        ".................................................."
        "................................................................................. 6",
        "2.2 Cross-site Request Forgery "
        "........................................................................... 7",
        "2.3 Information Disclosure "
        ".................................................."
        "............................................................................... 8"
    ]
    # Add the Table of Contents to the PDF
    for content in toc_content:
        pdf.ln(3)
        pdf.multi_cell(0, 5, content, align="L")


def section_content(pdf=pdf0):
    sections = [
        ("Confidentiality", [
            "This document contains sensitive and confidential information, it should not be shared with any "
            "other 3rd parties without written permission."]),
        ("GDPR", [
            "This document may contain personal data subject to the General Data Protection Regulation ("
            "GDPR). Handle any personal data in accordance with applicable data protection laws."]),
        ("Disclaimers", [
            "The information provided in this document is for general informational purposes only and should "
            "not be construed as professional advice. The author(s) disclaim any liability for damages "
            "arising from the use of this information."]),
        ("Change", [
            "The author(s) reserve the right to modify these terms. Review this document periodically for "
            "updates."]),
        ("Contact", ["For inquiries, contact:(+855) 875-248-05"])
    ]

    # Add text after Table of Contents
    pdf.add_page()

    pdf.ln(20)
    pdf.set_font("Arial", "B", 16)
    pdf.set_text_color(255, 0, 0)  # Red color
    pdf.cell(0, 10, "Legal", ln=1)

    # Loop through each section
    for heading, detail in sections:
        # Set font for heading
        pdf.set_font("Arial", "B", 12)
        pdf.set_text_color(255, 0, 0)  # Red color

        # Add heading text
        pdf.cell(0, 10, heading, ln=1)

        # Reset font to default
        pdf.set_font("Arial", "", 10)
        pdf.set_text_color(0, 0, 0)  # Reset color

        # Add content for the section
        for paragraph in detail:
            pdf.multi_cell(0, 5, paragraph, align="L")
            pdf.ln(3)

    pdf.set_left_margin(20)
    pdf.set_right_margin(20)


def change_log(pdf=pdf0):
    pdf.set_font("Arial", "B", 12)
    pdf.set_text_color(255, 0, 0)  # Red color
    pdf.cell(0, 10, "Change Log", ln=1)
    pdf.ln(1)  # Add space
    pdf.set_font("Arial", "", 10)
    pdf.set_text_color(0, 0, 0)  # Reset color

    # Define the table headers and data
    headers = ["Date", "Version", "Comments"]
    data = [
        ["1/12/2023", "0.1", "Initial Report"],
        ["2/12/2023", "0.2", "Recon Stage"],
        ["20/12/2023", "0.3", "Finalizing Stage"]
    ]
    # Calculate column widths based on available width
    available_width = pdf.w - pdf.l_margin - pdf.r_margin
    col_widths = [available_width / len(headers)] * len(headers)

    # Add table headers
    pdf.set_font("Arial", "B", 12)
    pdf.set_text_color(255, 0, 0)  # Red color
    for header, width in zip(headers, col_widths):
        pdf.cell(width, 10, header, border=1, align="C")
    pdf.ln()

    # Add table data
    pdf.set_font("Arial", "", 10)
    pdf.set_text_color(0, 0, 0)  # Reset color
    for row in data:
        for cell, width in zip(row, col_widths):
            pdf.cell(width, 10, cell, border=1, align="C")
        pdf.ln()
    # # Add text after images
    pdf.add_page()
    pdf.ln(20)


def executive_summary(pdf=pdf0):
    diagram_file = "flow1.png"
    # Set font to bold and red
    pdf.set_font("Arial", "B", 12)
    pdf.set_text_color(255, 0, 0)  # Red color

    # Add "Executive Summary" text
    pdf.cell(0, 10, "Executive Summary", ln=1)
    pdf.ln(5)
    # Reset font to default
    pdf.set_font("Arial", "", 10)
    pdf.set_text_color(0, 0, 0)  # Reset color

    # Add the rest of the text
    pdf.multi_cell(0, 5,
                   "CSTAD engaged CYBER-STAD to conduct a security assessment and penetration testing against "
                   "a website. The main goal of the engagement was to evaluate the security of the platform "
                   "and identify possible threats and vulnerabilities. This report details the scope of the "
                   "engagement, detailed information about all of the findings and some recommendations. The "
                   "summary below is intended for non-technical audiences to give an idea of the overall "
                   "results of the engagement and the key findings. The second section of this report is "
                   "intended for a technical audience as it lists all of our findings in detail, along with "
                   "reproduction steps, analysis, and recommendations. Based on the security assessment we "
                   "carried for [platform] and based on our findings, the current risk rating is high. The "
                   "vulnerabilities discovered can be used by malicious actors to cause breaches and even "
                   "gain unauthorized access to some management pages. The methodology followed is detailed "
                   "in the following diagram:",
                   align="L")

    pdf.image(diagram_file, x=35, y=100, w=150, h=90)


def scope(pdf=pdf0):
    pdf.add_page()

    pdf.set_left_margin(20)
    pdf.set_right_margin(20)
    pdf.ln(20)
    pdf.set_font("Arial", "B", 14)
    pdf.set_text_color(255, 0, 0)  # Red color
    pdf.cell(0, 10, "1 Engagement Summary", ln=1)

    # Add 1.1 Scope subsection
    pdf.set_font("Arial", "B", 12)
    pdf.set_text_color(255, 0, 0)  # Red color
    # pdf.cell(10)  # Add some indentation
    pdf.cell(0, 10, "1.1 Scope", ln=1)

    # Add content for 1.1 Scope
    scope_content = [  # LIST OF SCOPE_CONTENT DATA NEEDED
        "IP Address: 54.221.11.310",
        "cstad.shop",
        "food.cstad.shop",
        "coffee.cstad.shop",
        "koko.cstad.shop",
        "mama.cstad.shop",

    ]

    pdf.set_font("Arial", "U", 10)
    pdf.set_text_color(0, 0, 0)  # Reset color
    pdf.cell(0, 10, "As requested, the security assessment was only carried out on the following targets:",
             ln=1)

    # Add the content as a list
    for item in scope_content:
        pdf.cell(10)  # Add some indentation
        pdf.cell(0, 5, item, ln=1)


def risk_ratings(pdf=pdf0):
    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.set_text_color(255, 0, 0)  # Red color
    pdf.cell(0, 10, "1.2 Risk Ratings", ln=1)

    pdf.set_font("Arial", "", 10)
    pdf.set_text_color(0, 0, 0)  # Reset color
    pdf.multi_cell(0, 5,
                   "The vulnerability risk was calculated based on the Common Vulnerability Scoring System ("
                   "CVSS v3.0) which is the industry standard for assessing the severity of security "
                   "vulnerabilities.")
    pdf.multi_cell(0, 5,
                   "The table below gives a key to the risk naming and colours used throughout this report to "
                   "provide a clear and  concise risk scoring system. ")

    pdf.set_draw_color(0, 0, 0)
    pdf.set_line_width(0)

    # Risk table
    pdf.ln(5)  # Add space
    pdf.set_font("Arial", "", 9)
    pdf.set_text_color(0, 0, 0)

    # Define the table headers and data
    headers_risk = ["Risk", "CVSS v3.0 Score", "Recommendation"]
    data_risk = [
        ["None", "0.0", " N/A"],
        ["Low", "0.1 - 3.10", "Fix at the next update cycle."],
        ["Medium", "4.0 - 6.10", "Fix immediately if there are 0 high risk vulnerabilities."],
        ["High", "7.0 - 8.10", "Fix immediately if there are 0 critical vulnerabilities."],
        ["Critical", "10.0 - 10.0", "Fix immediately."]
    ]

    # Calculate column widths based on the longest string in each column
    col_widths_risk = [pdf.get_string_width(max(column, key=len)) + 25 for column in zip(*data_risk)]

    # Add table headers
    pdf.set_font("Arial", "B", 12)
    pdf.set_text_color(255, 0, 0)  # Red color
    for header_risk, width in zip(headers_risk, col_widths_risk):
        pdf.cell(width, 10, header_risk, border=1, align="C")
    pdf.ln()

    # Add table data
    pdf.set_font("Arial", "", 10)
    pdf.set_text_color(0, 0, 0)  # Reset color
    for row_risk in data_risk:
        for cell_risk, width in zip(row_risk, col_widths_risk):
            pdf.cell(width, 10, cell_risk, border=1)
        pdf.ln()


def finding_overviews(pdf=pdf0):
    pdf.set_left_margin(20)
    pdf.set_right_margin(20)
    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    pdf.set_text_color(255, 0, 0)  # Red color
    pdf.cell(0, 10, "1.3 Findings Overview", ln=1)
    pdf.ln(5)
    pdf.set_font("Arial", "", 10)
    pdf.set_text_color(0, 0, 0)  # Reset color
    pdf.multi_cell(0, 5,
                   "Below is a list of all the issues found during the engagement along with a brief "
                   "description, its impact and the risk rating associated with it. Please refer to the 'Risk "
                   "Ratings' section for more information on how this is calculated.")

    pdf.ln(5)

    # Define the get_background_color function
    def get_background_color(risk_level):
        risk_level_lower = risk_level.lower()
        if "critical" in risk_level_lower:
            return 255, 0, 0  # Red
        elif "medium" in risk_level_lower:
            return 255, 165, 0  # Orange
        elif "hard" in risk_level_lower:
            return 255, 255, 0  # Yellow
        elif "low" in risk_level_lower:
            return 0, 255, 0  # Green
        else:
            return 255, 255, 255  # White

    # Define the table headers and data for the new table
    pdf.ln(5)
    headers_findings = ["ID", "Risk", "Description"]  # List of headers_findings are needed
    # List of data_findings are needed too
    data_findings = [
        ["1", "Hard", "SQL Injection leading to unauthorized database access."],
        ["2", "medium", "CSRF - Clients can be forced to submit certain non-critical requests."],
        ["3", "low", "PHP version disclosure - Can help develop attacks for this specific version."]
    ]

    # Calculate column widths based on the longest string in each column
    col_widths_findings = [pdf.get_string_width(max(column, key=len)) + 17 for column in zip(*data_findings)]

    # Add table headers
    pdf.set_font("Arial", "B", 12)
    pdf.set_text_color(255, 0, 0)  # Red color
    for header_findings, width in zip(headers_findings, col_widths_findings):
        pdf.cell(width, 10, header_findings, border=1, align="C")
    pdf.ln()

    # Add table data with dynamic background color
    pdf.set_font("Arial", "", 10)
    pdf.set_text_color(0, 0, 0)  # Red color
    for row_findings in data_findings:
        for index, (cell_findings, width) in enumerate(zip(row_findings, col_widths_findings)):
            if headers_findings[index] == "Risk":
                # Get dynamic background color based on risk level
                background_color = get_background_color(row_findings[1])  # Use the content of the "Risk" cell
                pdf.set_fill_color(*background_color)
            else:
                # Default white background for other cells
                pdf.set_fill_color(255, 255, 255)

            pdf.cell(width, 10, cell_findings, border=1, fill=True)
        pdf.ln()


def sql_injection_report(pdf=pdf0):
    pdf.set_font("Arial", "B", 12)  # Set the font to bold, size 14
    pdf.cell(0, 5, "2.1 SQL Injection    CRITICAL      ID: 1", ln=True)
    pdf.ln(3)

    # Set the font to bold, size 10, and red color for the description
    pdf.set_font("Arial", "", 10)
    pdf.set_text_color(0, 0, 0)  # Red color
    pdf.multi_cell(0, 5,
                   "We discovered that using specially crafted requests a malicious actor can communicate "
                   "with the database and query it to retrieve stored data including data stored in the users "
                   "tables.")
    pdf.ln()

    # Define the table data for vulnerability details
    data_vulnerability = [
        ["URL", "https://food.cstad.shop"],
        ["Parameter", "id"],
        ["References", "https://owasp.org/www-community/attacks/SQL_Injection"],
        ["Request",
         "POST rest/user/login HTTP/1.1\nHost: domain.shop\nAccept: application/json, text/plain, */*"],
        ["Response", "HTTP/1.1 200 OK\nContent-Type: application/json; charset=utf-8\nVary: Accept-Encoding"]
        # Add more details as needed
    ]
    # Calculate column widths based on the longest string in each column
    col_widths_vulnerability = [pdf.get_string_width(max(column, key=len)) + 15 for column in
                                zip(*data_vulnerability)]

    # Add table data with bold headers
    pdf.set_font("Arial", "B", 10)  # Set the font to bold for headers
    for row_vulnerability in data_vulnerability:
        for index, (cell_vulnerability, width) in enumerate(zip(row_vulnerability, col_widths_vulnerability)):
            if index == 0:  # Bold only the first cell (header)
                pdf.set_font("Arial", "B", 10)
            else:
                pdf.set_font("Arial", "", 10)

            pdf.cell(width, 10, cell_vulnerability, border=1)
        pdf.ln()

    # Set the font back to regular
    pdf.set_font("Arial", "", 10)


def way_to_mitigate_sql_injection(pdf=pdf0, content=mitigate_sql_injection):
    pdf.ln(5)
    # Add vulnerability details to the report as a table

    pdf.set_font("Arial", "B", 12)  # Set the font to bold, size 14
    pdf.cell(0, 5, "[+] How to prevent SQL Injection CRITICAL      ID: 1", ln=True)
    pdf.ln(3)

    # Set the font to bold, size 10, and red color for the description
    pdf.set_font("Arial", "", 10)
    pdf.set_text_color(0, 0, 0)  # Red color
    pdf.multi_cell(0, 5,
                   content)


class Report:
    pdf = FPDF("P", "mm", "A4")

    def __init__(self):
        self.data = 'abc'  # Initialize to False or true to check conditions (static)
        self.output_path = Path(__file__).parent / "output"
        self.output_path.mkdir(parents=True, exist_ok=True)

    def generate_report(self, pdf=pdf):
        file_name = "report.pdf"
        if self.data == '':  # false
            print("No data available to generate a report, start exploit first.")
        else:
            print(f"[+] Generating report ---> {file_name} ...")

            # Specify the file names for header and content images
            header_file = "CSTAD.png"
            # pdf = FPDF("P", "mm", "A4")
            pdf.add_page()
            # add header image (will be code it later, but let me put the screen short first)
            pdf.ln(10)
            pdf.image(header_file, x=54, y=4, w=100, h=32)
            # Date
            pdf.set_y(60)
            pdf.set_left_margin(20)
            pdf.set_right_margin(20)
            pdf.set_font("Arial", "U", 12)
            pdf.set_text_color(255, 0, 0)  # Red color
            # Add "Table of Contents" text
            pdf.cell(0, 10, f"Date: [{formatted_date}]", ln=1)
            pdf.set_text_color(0, 0, 0)  # reset color
            # Client details
            customer_contact_detail(pdf=pdf)
            # content table
            content_table(pdf=pdf)
            # section content
            section_content(pdf=pdf)
            # change log
            change_log(pdf=pdf)
            # executive summary
            executive_summary(pdf=pdf)
            # -------------------------------pie chart start--------------------------------------------
            # Add section for pie chart
            pdf.ln(100)
            pdf.set_font("Arial", "", 10)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(0, 10, "The following charts summarize the findings grouped by severity of the threat:", ln=1,
                     align="L")
            pdf.add_page()
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 5, "Vulnerabilities Breakdown", ln=1, align="C")

            # Static data for vulnerabilities breakdown
            # Dictionary OF vulnerabilities_data DATA NEEDED
            vulnerabilities_data = {
                'Low': 28,
                'Medium': 22,
                'High': 43 + 24,
                'Critical': 37 + 14
            }
            pdf.ln(10)
            # # Generate pie chart
            chart_width = 640
            chart_height = 480
            chart_data = list(vulnerabilities_data.values())
            chart_labels = list(vulnerabilities_data.keys())
            chart_colors = ['#00FF00', '#FFFF00', '#FFA500', '#FF0000']

            img_path = generate_pie_chart(chart_data, chart_labels, chart_colors)
            pdf.image(img_path, x=20, y=20, w=160)
            # # bar chart ---------------start------------------------
            # Generate bar chart
            bar_chart_width = 640
            bar_chart_height = 480
            bar_chart_data = list(vulnerabilities_data.values())
            bar_chart_labels = list(vulnerabilities_data.keys())
            bar_chart_colors = ['#00FF00', '#FFFF00', '#FFA500', '#FF0000']
            bar_image_path = generate_bar_chart_image(categories=bar_chart_labels, values=bar_chart_data,
                                                      colors=bar_chart_colors)
            pdf.image(bar_image_path, x=20, y=140, w=160)
            # # -------------------------------end---------------------------------
            # Add Engagement Summary section
            # Scope
            scope(pdf=pdf)
            # risk rating
            risk_ratings(pdf=pdf)
            # 1.3 finding overview
            # pdf.add_page()
            finding_overviews(pdf=pdf)
            # Add 2 Technical Details section title
            # pdf.add_page()
            pdf.ln(10)
            pdf.set_font("Arial", "B", 14)
            pdf.set_text_color(255, 0, 0)  # Red color
            pdf.cell(0, 10, "2 Technical Details", ln=True)
            pdf.ln(5)
            # Add vulnerability details to the report as a table
            # SQL Injection
            sql_injection_report(pdf=pdf)
            # Way to mitigate SQL injection attacks
            way_to_mitigate_sql_injection(pdf=pdf)

            pdf.output(str(self.output_path / file_name), "F")
            location = """file:///D:/Multi-programming_languages/Python/CYBER-STAD%20tool%20for%20final%20project/cyber_stad_tool_v1/view/generate_reports/output/report.pdf"""
            print(f"=> File Pen-testing reported: {location}")

