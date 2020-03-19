class lzw_algoritma():

	def char_tespit(self):
		myli1 = []
		for i in xrange(len(self.metin)):
			if self.metin[i] not in myli1:
				myli1.append(self.metin[i])
		return myli1


	def index_ata(self, kl): #liste verilecek char_tespit ciktisi <- Karakter Listesi
		self.mysoz = [["", ""]]
		added = []
		self.sayac = 0
		for c in kl:
			if c not in added:
				self.mysoz.append([c, self.sayac])
				added.append(c)
				self.sayac += 1


	def sifrele(self):
		mystr = ""
		self.out = ""
		for karakter in self.metin:
			sc = mystr + karakter
			kontrol = "yok"
			for dene in self.mysoz:
				if sc == dene[0]:
					kontrol = "var"
			if kontrol == "var":
				mystr += karakter
			else:
				self.mysoz.append([sc, self.sayac])
				for dene in self.mysoz:
					if mystr == dene[0]:
						self.out += str(dene[1])
				self.sayac += 1
				mystr = karakter
		for dene in self.mysoz:
			if mystr == dene[0]:
				self.out += str(dene[1])



	def cikti(self, giris):
		self.metin = giris
		self.index_ata(self.char_tespit())
		self.sifrele()
		return self.out, self.mysoz
