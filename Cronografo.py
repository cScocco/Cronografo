import tkinter as tk
from tkinter.font import Font


class Cronografo(tk.Frame):
    __tempo_attesa = 10  # 10 centesimi di secondo

    def __init__(self, master=None):  # master è il widget genitore
        # inizializzazione del frame
        super().__init__(master)
        self.grid()  # layout a griglia
        # campo display
        self.vDisplay = tk.StringVar()  # variabile da abbinare al campo
        display_font = Font(size=24)
        self.txt_display = tk.Entry(self, textvariable=self.vDisplay, width=8,
                                    justify=tk.CENTER, state=tk.DISABLED, font=display_font)
        self.txt_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        # pulsante start/stop
        self.btn_start_stop = tk.Button(self, text="start/stop", command=self.start_stop)
        self.btn_start_stop.grid(row=1, column=0)
        # pulsante reset
        self.btn_reset = tk.Button(self, text="reset", command=self.reset)
        self.btn_reset.grid(row=1, column=1)
        # reset timer
        self.reset()
        # blocco le dimensioni della finestra
        self.master.resizable(0, 0)
        # loop di attesa eventi
        self.mainloop()

    def display_time(self):
        minuti = self.__counter // 6000  # divisione intera
        secondi = (self.__counter % 6000) // 100
        centesimi = (self.__counter % 6000) % 100
        self.vDisplay.set(f'{minuti:02d}:{secondi:02d}.{centesimi:02d}')

    def increment_time(self):
        if self.__isRunning:
            self.__counter += 1  # contatore di centesimi
            self.display_time()
            self.after(Cronografo.__tempo_attesa, self.increment_time)

    def start_stop(self):
        self.__isRunning = not self.__isRunning  # cambio lo stato del cronografo
        if self.__isRunning:
            self.after(Cronografo.__tempo_attesa, self.increment_time)

    def reset(self):
        self.__isRunning = False
        self.__counter = 0
        self.display_time()


if __name__ == '__main__':
    def main():
        Cronografo(tk.Tk())


    main()
