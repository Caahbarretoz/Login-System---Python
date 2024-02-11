import customtkinter
from PIL import Image
import os
from sys import platform

width = 700
height = 400

root = customtkinter.CTk()
root.title("Login System")


x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 3) - (height // 3)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.resizable(False, False)

root.iconbitmap('./pictures/gsnakeicon.ico')

current_path = os.path.dirname((os.path.realpath(__file__)))

bg_image = customtkinter.CTkImage(Image.open(current_path + "./pictures/background.png"),
                                             size = (width, height))

application_logo = customtkinter.CTkImage(Image.open(current_path + "./pictures/snake.png"),
                                             size = (35, 35))


user_image = customtkinter.CTkImage(Image.open(current_path + "./pictures/user.png"),
                                             size = (70, 70))

login_image = customtkinter.CTkImage(Image.open(current_path + "./pictures/enter.png"),
                                             size = (15, 15))


bg_image_label = customtkinter.CTkLabel(root, image=bg_image, text="")
bg_image_label.grid(row=0, column=0, padx=(0, 170), pady=(0, 70))

logo = customtkinter.CTkLabel(root,
                              text="",
                              image=application_logo,
                              fg_color="transparent",
                              bg_color="transparent"
                              )
logo.grid(row=0, column=0, padx=(100, 20), pady=(0, 422))

logo_text = customtkinter.CTkLabel(root,
                                   text="Python Login",
                                   font=("Roboto bold", 22),
                                   text_color="black"
                                   )
logo_text.grid(row=0, column=0, padx=(270, 20), pady=(0, 422))

user_label = customtkinter.CTkLabel(root,
                                    text="",
                                    image=user_image,
                                    anchor="n",
                                    compound="top",
                                    fg_color="#3f3d3e"
                                    )
user_label.grid(row=0, column=0, padx=(0, 530), pady=(54, 240))

username = customtkinter.CTkEntry(root,
                                  placeholder_text="Username",
                                  corner_radius=7,
                                  fg_color="#3f3d3e",
                                  bg_color="#3f3d3e",
                                  #border_width=0,
                                  width=145,
                                  height=27,
                                  placeholder_text_color="black",
                                  border_color="black",
                                  text_color="black"
                                  )
username.grid(row=0, column=0, padx=(0, 530), pady=(25, 75))

password = customtkinter.CTkEntry(root,
                                  placeholder_text="Password",
                                  corner_radius=7,
                                  fg_color="#3f3d3e",
                                  bg_color="#3f3d3e",
                                  #border_width=0,
                                  width=145,
                                  height=27,
                                  placeholder_text_color="black",
                                  border_color="black",
                                  show="*",
                                  text_color="black"
                                  )
password.grid(row=0, column=0, padx=(0, 530), pady=(60, 40))

login_btn = customtkinter.CTkButton(root,
                                    text="Login",
                                    corner_radius=7,
                                    fg_color="#3f3d3e",
                                    bg_color="#3f3d3e",
                                    border_width=2,
                                    width=110,
                                    height=25,
                                    border_color="black",
                                    text_color="black",
                                    image=login_image,
                                    compound="right",
                                    font=("Roboto bold", 13)
                                    )
login_btn.grid(row=0, column=0, padx=(0, 530), pady=(93, 7))

remember_me = customtkinter.CTkCheckBox(root,
                                        text="Remember me",
                                        corner_radius=7,
                                        fg_color="#3f3d3e",
                                        bg_color="#3f3d3e",
                                        border_width=2,
                                        width=110,
                                        height=25,
                                        border_color="black",
                                        text_color="black",
                                        font=("Roboto bold", 13),
                                        checkmark_color="#bf0634",
                                        )
remember_me.grid(row=0, column=0, padx=(0, 300), pady=(93, 7))

not_member = customtkinter.CTkLabel(root,
                                    text="Not a member?",
                                    corner_radius=7,
                                    width=110,
                                    height=25,
                                    text_color="black",
                                    font=("Roboto bold", 15)
                                    )
not_member.grid(row=0, column=0, padx=(270, 20), pady=(25, 75))

sign_btn = customtkinter.CTkButton(root,
                                    text="Sign Up",
                                    corner_radius=7,
                                    fg_color="#bf0634",
                                    bg_color="transparent",
                                    border_width=2,
                                    width=110,
                                    height=25,
                                    border_color="black",
                                    text_color="black",
                                    compound="right",
                                    font=("Roboto bold", 13)
                                    )
sign_btn.grid(row=0, column=0, padx=(270, 20), pady=(60, 40))

forgot_password = customtkinter.CTkButton(root,
                                    text="Forgot password?",
                                    corner_radius=7,
                                    fg_color="#bf0634",
                                    bg_color="transparent",
                                    border_width=2,
                                    width=110,
                                    height=25,
                                    border_color="black",
                                    text_color="black",
                                    compound="right",
                                    font=("Roboto bold", 13),
                                    hover_color="#660000"
                                    )
forgot_password.grid(row=0, column=0, padx=(270, 20), pady=(95, 5))

root.mainloop()
