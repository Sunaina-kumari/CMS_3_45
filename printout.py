import os
from fpdf import FPDF

#institutename
        # addresss
        #contact
        #Rollno'Name''Gender'Phone No''Address''Department''Course''DOB'

company="GTB institute "
address="Jalandhar"
contact="98989898"

class my_cust_PDF(FPDF):
    def header(self):
        self.set_text_color(21, 18, 225)
        self.set_font('Helvetica', 'B', 20)
        w = self.get_string_width(company) + 6
        self.set_x((210 - w) / 2)
        self.cell(w, 9, company)
        self.ln(10) # line break


        self.set_text_color(18, 225, 21 )
        self.set_font('Helvetica', 'B', 12)
        w = self.get_string_width(address) + 6
        self.set_x((210 - w) / 2)
        self.cell(w, 9, address)
        self.ln(10)

        w = self.get_string_width(contact) + 6
        self.set_x((210 - w) / 2)
        self.cell(w, 9, contact)
        self.ln(10)

        self.ln(20)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_content(self,data):


        self.set_fill_color(200, 220, 255)
        self.ln()
        self.ln()


        self.set_font('Arial', 'B', 11)
        spacing=1
        col_width = self.w /9   # 9 = no of columns +1 to adjust columns to screen
        row_height = self.font_size+2


        #Table heading
        headings = ['Rollno','Name','Gender','Phone No','Address','Department','Course','DOB']
        for i in headings:  # for headings
            self.cell(col_width, row_height * spacing, txt=i, border=1)
        self.ln(row_height * spacing)

        #table body
        self.set_font('Arial', '', 11)
        for row in data:
            for item in row:
                self.cell(col_width, row_height * spacing, txt=str(item), border=1)
            self.ln(row_height * spacing)
        # Line break

        self.ln()


        # Mention in italics
        self.ln()
        self.ln()
        self.ln()
        self.set_font('', 'I')
        text1 = '(---------------------  end of page  -----------------------)'
        w = self.get_string_width(text1) + 6
        self.set_x((210 - w) / 2)
        self.cell(0, 6, text1)

    def print_chapter(self,data):
        self.add_page()   #header,footer
        self.chapter_content(data)

if __name__ == '__main__':
    pdf = my_cust_PDF()
    data=[['Rollno','Name','Gender','Phone No','Address','Department','Course','DOB'],
          ['Rollno','Name','Gender','Phone No','Address','Department','Course','DOB'],
          ['Rollno','Name','Gender','Phone No','Address','Department','Course','DOB']]

    pdf.print_chapter(data)
    os.remove('pdf_file1.pdf')
    pdf.output('pdf_file1.pdf')
    os.system('explorer.exe "pdf_file1.pdf"')