from tkinter import Button, Entry, Scrollbar, Tk, Label, Text
from tkinter.constants import DISABLED, END, NORMAL, TRUE
from chat_fxn import get_response, bot_name

# defining colors
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TXT_COLOR = "#EAECEE"

# defining fonts
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

# building the app
class ChatbotApp:

    def __init__( self ):
        self.window = Tk()
        self._setup_main_window()

    def run( self ):
        self.window.mainloop()

    def _setup_main_window( self ):
        self.window.title( "Chat With Me :-)" )
        self.window.resizable( width=TRUE, height=False )
        self.window.configure( width=470, height=520, bg=BG_COLOR )

        # head label
        head_label = Label( self.window, bg=BG_COLOR, fg=TXT_COLOR,
                            text="Welcome to IntroVerse", font=FONT_BOLD, pady=10 )
        head_label.place( relwidth=1 )

        # tiny divider
        line = Label( self.window, width=450, bg=BG_GRAY )
        line.place( relwidth=1, rely=0.07, relheight=0.012 )

        # text widget
        self.text_widget = Text( self.window, width=20, height=2, bg=BG_COLOR,
                                fg=TXT_COLOR, font=FONT, padx=5, pady=5 )
        self.text_widget.place( relheight=0.745, relwidth=1, rely=0.08 )
        self.text_widget.configure( cursor="arrow", state=DISABLED )

        # scroll bar
        scrollbar = Scrollbar( self.text_widget )
        scrollbar.place( relheight=1, relx=0.974 )
        scrollbar.configure( command=self.text_widget.yview )

        # button label
        button_label = Label( self.window, bg=BG_GRAY, height=80 )
        button_label.place( relwidth=1, rely=0.825 )

        # message box
        self.msg_entry = Entry( button_label, bg="#2C3E50", fg=TXT_COLOR, font=FONT )
        self.msg_entry.place( relwidth=0.74, relheight=0.03, rely=0.008, relx=0.011 )
        self.msg_entry.focus()
        self.msg_entry.bind( "<Return>", self._on_enter_pressed )

        # send button
        send_button = Button( button_label, text="Send", font=FONT_BOLD, width=20,
                                bg=BG_GRAY, command=lambda: self._on_enter_pressed(None) )
        send_button.place( relx=0.77, rely=0.008, relheight=0.03, relwidth=0.223 )

    def _on_enter_pressed( self, event ):
        msg = self.msg_entry.get()
        self._insert_message( msg, "You" )

    def _insert_message( self, msg, sender ):
        if not msg:
            return

        self.msg_entry.delete( 0, END )
        msg_1 = f"{ sender }: { msg }\n\n"
        self.text_widget.configure(  state=NORMAL )
        self.text_widget.insert( END, msg_1 )
        self.text_widget.configure( state=DISABLED )


        msg_2 = f"{ bot_name }: { get_response(msg) }\n\n"
        self.text_widget.configure(  state=NORMAL )
        self.text_widget.insert( END, msg_2 )
        self.text_widget.configure( state=DISABLED )

        self.text_widget.see( END )

if __name__ == "__main__":
    app = ChatbotApp()
    app.run()