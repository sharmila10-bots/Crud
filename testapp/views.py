from django.shortcuts import render,redirect
from testapp.models import Book
from testapp import forms

# Create your views here.
#retrieve data
def read_data(request):
    book=Book.objects.all()
    my_dict={'book':book}
    return render(request,'html/home.html',my_dict)

#insert data
def insert_data(request):
    form=forms.BookForm()
    my_dict={'form':form}
    if request.method=='POST':
        form=forms.BookForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/retrieve')

    return render(request,'html/insert.html',my_dict)

#delete data
def delete_data(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect('/retrieve')

#update data
def update_data(request,id):
    book=Book.objects.get(id=id)
    my_dict={'book':book}
    if request.method=='POST':
        form=forms.BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
        return redirect('/retrieve')
    return render(request,'html/update.html',my_dict)
