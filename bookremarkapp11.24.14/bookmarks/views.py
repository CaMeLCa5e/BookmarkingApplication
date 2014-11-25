from django.shortcuts import render
from django.http      import HttpResponse
from django.template  import loader
from django.template  import RequestContext


from models import LinkList
from models import Link


def index(request):
  '''static page showing links to all the required features'''
  template      = loader.get_template('bookmarks/index.html')
  context       = RequestContext(request)
  return HttpResponse(template.render(context))



def listalllinklist(request):
  '''lists all the Link List objects'''
  all_linklists = LinkList.objects.all()
  template      = loader.get_template('bookmarks/listalllinklists.html')
  context       = RequestContext(request, {'all_linklists': all_linklists,})
  return HttpResponse(template.render(context))



def createlinklist(request):
  '''page for generating new Link Lists'''
  template      = loader.get_template('bookmarks/linklistcreate.html')
  context       = RequestContext(request)
  return HttpResponse(template.render(context))



def createlinklistpost(request):
  '''process all create requests'''
  linklist      = LinkList(name=request.POST['name'])
  linklist.save()
  template      = loader.get_template('bookmarks/linklistcreatepost.html')
  context       = RequestContext(request, {'linklist': linklist,})
  return HttpResponse(template.render(context))



def linklistcreateaddlink(request, linklist_id):
  ''' nearly static page for creating a new Link and adding it to a Link List.
      pass link list ID through the template form as a hidden form field.'''
  template      = loader.get_template('bookmarks/linklistcreateaddlink.html')
  context       = RequestContext(request, {'linklist_id': linklist_id,})
  return HttpResponse(template.render(context))



def linklistcreateaddlinkpost(request):
  ''' create a new link, add it to an existing link list, then save to storage '''
  (name, link, tags, linklist_id) = map(lambda var_name: request.POST[var_name], ['name', 'url', 'tags', 'linklist_id'])
  # create a new link
  new_link = Link(name=name, link=link, tags=tags)
  new_link.save()
  # add id to the new link
  linklist = LinkList.objects.get(id=linklist_id)
  # add link to db
  linklist.links.add(new_link)
  linklist.save()
  # return the success page
  template      = loader.get_template('bookmarks/linklistcreateaddlinkpost.html')
  context       = RequestContext(request, {'linklist': linklist,})
  return HttpResponse(template.render(context))



def retrievelinklist(request, linklist_id):
  ''' load and display a list object keying off its ID. '''
  linklist = LinkList.objects.get(id=linklist_id)
  template      = loader.get_template('bookmarks/linklistretrieve.html')
  context       = RequestContext(request, {'linklist': linklist,})
  return HttpResponse(template.render(context))



def updatelinklist(request, linklist_id):
  return HttpResponse('Update LinkList page! ID == {0}'.format(linklist_id))



def deletelinklist(request, linklist_id):
  return HttpResponse('Delete LinkList page! ID == {0}'.format(linklist_id))



# link object views
def createlink(request):
  return HttpResponse('Create Link page')


def retrievelink(request, link_id):
  return HttpResponse('Retrieve Link page ID == {0}'.format(link_id))


def updatelink(request, link_id):
  return HttpResponse('Update Link page ID == {0}'.format(link_id))


def deletelink(request, link_id):
  link = Link.objects.get(id=link_id)
  name = link.name
  link.delete()
  return HttpResponse("You deleted Link ID == {0}, Name == '{1}'".format(link_id, name))


def listalllink(request):
  return HttpResponse('List All Links')
  





