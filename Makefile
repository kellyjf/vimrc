
NHOME := $(HOME)/.config/nvim

install:
	mkdir -p $(NHOME)/.config/nvim/
	cp $(HOME)/.vim/rc $(HOME)/.vimrc
	cp  -r $(HOME)/.vim/init.vim autoload $(NHOME)/


