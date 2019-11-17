
NHOME := $(HOME)/.config/nvim

install:
	mkdir -p $(NHOME)
	cp $(HOME)/.vim/rc $(HOME)/.vimrc
	cp  -r $(HOME)/.vim/init.vim autoload $(NHOME)/


