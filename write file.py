
f=open("student.txt","a") # here "a" means append a new line to text file,,,a er jaygay "w" dile file override hobe,mane agergula
#muche notungula thakbe shudhu

f.write("\n oi barir selina \n tar sathe khelina")

f.close()
#file jodi age theke na thake r write korte cai tahole auto file create hoye jabe notun text niye
f=open("student1.txt","a")
f.write("\n oi barir selina \n tar sathe khelina")

f.close()

#  Html file add korte caile
f=open("hello.html","w")
f.write("<h1> oi barir selina \n tar sathe khelina<h1>")

f.close()
