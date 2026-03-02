import sys

        clear_btn = QPushButton("Clear")
        clear_btn.clicked.connect(self.clear_canvas)

        exit_btn = QPushButton("Exit")
        exit_btn.clicked.connect(self.close)

        toolbar.addWidget(draw_btn)
        toolbar.addWidget(erase_btn)
        toolbar.addWidget(clear_btn)
        toolbar.addWidget(exit_btn)

        layout.addLayout(toolbar)
        self.setLayout(layout)

    def set_draw_mode(self):
        self.eraser_mode = False

    def set_eraser_mode(self):
        self.eraser_mode = True

    def clear_canvas(self):
        self.canvas.fill(Qt.transparent)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.canvas)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        if self.drawing:
            painter = QPainter(self.canvas)

            if self.eraser_mode:
                painter.setCompositionMode(QPainter.CompositionMode_Clear)
                pen = QPen(Qt.transparent, 20)
            else:
                pen = QPen(self.brush_color, self.brush_size)

            pen.setCapStyle(Qt.RoundCap)
            painter.setPen(pen)
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TransparentDraw()
    window.show()
