from django.urls import path, re_path
from . import views
from . import api

urlpatterns = [

    
    
    
    path('api/catagory/delete/<int:pk>',api.CatagoryDeleteApi.as_view()),
    
    path('api/catagory/update/<int:pk>',api.CatagoryUpdateApi.as_view()),
    
    path('api/catagory',api.CatagoryApi.as_view()),
    path('api/catagory/create', api.CatagoryCreateApi.as_view(),name="api_catagory_create"),

    
    path('api/assignitem/delete/<int:pk>',api.TeamDeleteApi.as_view()),
    
    path('api/assignitem/update/<int:pk>',api.TeamUpdateApi.as_view()),
    
    path('api/assignitem',api.TeamApi.as_view()),
    path('api/assignitem/create', api.TeamCreateApi.as_view()),

    path('api/team/delete/<int:pk>',api.TeamDeleteApi.as_view()),
    
    path('api/team/update/<int:pk>',api.TeamUpdateApi.as_view()),
    
    path('api/team',api.TeamApi.as_view()),
    path('api/team/create', api.TeamCreateApi.as_view(),name="api_team_create"),
    
    path('api/item/delete/<int:pk>',api.ItemDeleteApi.as_view()),
    
    path('api/item/update/<int:pk>',api.ItemUpdateApi.as_view()),
    
    path('api/item',api.ItemApi.as_view()),
    path('api/item/create', api.ItemCreateApi.as_view(),name="api_item_create"),
    
    path('api/employee/delete/<int:pk>',api.EmployeeDeleteApi.as_view()),
    
    path('api/employee/update/<int:pk>',api.EmployeeUpdateApi.as_view()),
    
    path('api/employee',api.EmployeeApi.as_view()),
    path('api/employee/create', api.EmployeeCreateApi.as_view(), name="api_employee_create"),
    
    # The home page
    # path('', views.index, name='signin'),
    # path('home/', views.index, name='home'),
    path("index/", views.IndexView.as_view(), name="index"),
    path('search/',views.SearchResultsView.as_view(),name='search'),
    # path("employee_list/", views.Employees.as_view(), name="employee_list"),
    path("employee_list/", views.EmployeesListView.as_view(), name="employee_list"),
    path("gadgets_list/", views.Gadgets.as_view(), name="gadgets_list"),
    path("assign_item_create/", views.AssignItemsCreateView.as_view(), name="assign_item_create"),
    # path("assign_item_delete/<int:pk>", views.AssignItemsDeleteView.as_view(), name="assign_item_delete"),
    path("team_list/", views.Teams.as_view(), name="team_list"),
    path("catagory/", views.Catagorys.as_view(), name="catagory"),
    path("employee_delete/<int:pk>", views.EmployeeDeleteView.as_view(), name="employee_delete"),
    path("gadgets_delete/<int:pk>", views.GadgetsDeleteView.as_view(), name="gadgets_delete"),
    path("team_delete/<int:pk>", views.TeamsDeleteView.as_view(), name="team_delete"),
    path("assign_item_delete/<int:pk>", views.AssignItemsDeleteView.as_view(), name="assign_item_delete"),
    path("catagory_delete/<int:pk>", views.CategorysDeleteView.as_view(), name="catagory_delete"),
    path("employee_update/<int:pk>", views.EmployeeUpdateView.as_view(), name="employee_update"),
    path("gadgets_update/<int:pk>", views.GadgetsUpdateView.as_view(), name="gadgets_update"),
    path("team_update/<int:pk>", views.TeamsUpdateView.as_view(), name="team_update"),
    path("catagory_update/<int:pk>", views.CatagorysUpdateView.as_view(), name="catagory_update"),
    path("employee_create/", views.EmployeesCreateView.as_view(), name="employee_create"),
    path("gadgets_create/", views.GadgetsCreateView.as_view(), name="gadgets_create"),

    path('tran/', views.tran, name='tran'),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('charge/', views.charge, name='charge'),
    # path('config/', views.stripe_config),
    # path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.SuccessView.as_view(),name="success"),
    path('cancelled/', views.CancelledView.as_view()),





]







    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),


