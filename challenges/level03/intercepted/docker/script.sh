var=1
for file in /work/ticket/*
do
        convert ticket/kerberos_$var.jpg -crop 698x100+0+115 kerb_crop/kerberos_$var.jpg
        tesseract /work/kerb_crop/kerberos_$var.jpg res 2&>/dev/null ; cat res.txt | tr -d ' ' | grep "\S" >> ticket.txt
        echo $var
        ((var=var+1))
done
