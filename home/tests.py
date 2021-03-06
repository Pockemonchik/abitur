<!-- <html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">


    <link rel="canonical" href="https://getbootstrap.com/docs/4.5/examples/checkout/">

    <!-- Bootstrap core CSS -->
<!-- <link href="bootstrap.min.css" rel="stylesheet"> -->

    <!-- Favicons -->
<!-- <link rel="apple-touch-icon" href="/docs/4.5/assets/img/favicons/apple-touch-icon.png" sizes="180x180">
<link rel="icon" href="/docs/4.5/assets/img/favicons/favicon-32x32.png" sizes="32x32" type="image/png">
<link rel="icon" href="/docs/4.5/assets/img/favicons/favicon-16x16.png" sizes="16x16" type="image/png">
<link rel="manifest" href="/docs/4.5/assets/img/favicons/manifest.json">
<link rel="mask-icon" href="/docs/4.5/assets/img/favicons/safari-pinned-tab.svg" color="#563d7c">
<link rel="icon" href="/docs/4.5/assets/img/favicons/favicon.ico">
<meta name="msapplication-config" content="/docs/4.5/assets/img/favicons/browserconfig.xml">
<meta name="theme-color" content="#563d7c"> --> -->


    <!-- <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
    </style>
    <!-- Custom styles for this template -->
    <!-- <link href="form-validation.css" rel="stylesheet">
  </head> -->
  <!-- <body> --> -->
  {% extends "base.html" %}
  {%load static%}
  {% block content %}

<div class="pricing-header px-3 py-3 pt-md-5 pb-md-4 mx-auto text-center">
  <h1 class="display-4">Панель администратора</h1>

</div>

<div class="container">
  <div class="card-deck mb-3 text-center">
    <div class="card mb-4 shadow-sm">
      <div class="card-header">
        <h4 class="my-0 font-weight-normal"></h4>
      </div>
      <div class="card-body">
          <ul class="list-unstyled mt-3 mb-4">
            <li><a href="{%url 'adminpanel' slug='1факультет'%}">1факультет</a></li>
            <li><a href="{%url 'adminpanel' slug='2факультет'%}">2факультет</a></li>
            <li><a href="{%url 'adminpanel' slug='3факультет'%}">3факультет</a></li>
            <li><a href="{%url 'adminpanel' slug='4факультет'%}">4факультет</a></li>
            <li>Факультет</li>
        </ul>

      </div>
    </div>
    <div class="card mb-4 shadow-sm">
      <div class="card-header">
        <h4 class="my-0 font-weight-normal"></h4>
      </div>
      <div class="card-body">
        <ul class="list-unstyled mt-3 mb-4">
          <li>Факультет</li>
          <li>Факультет</li>
          <li>Факультет</li>

        </ul>

      </div>
    </div>
    <div class="card mb-4 shadow-sm">
      <div class="card-header">
        <h4 class="my-0 font-weight-normal"></h4>
      </div>
      <div class="card-body">
        <ul class="list-unstyled mt-3 mb-4">
          <li>Факультет</li>
          <li>Факультет</li>
          <li>Факультет</li>
        </ul>

      </div>
    </div>
  </div>
      <form  action="{%url 'saveAdminTable' slug %}" method="post">
          {% csrf_token %}
    <table class="table table-bordered">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Фамилия</th>
            <th scope="col">допуск</th>
            <th scope="col">кол-во баллов</th>
            <th scope="col">пометка</th>
          </tr>
        </thead>
        <tbody>

            {{ form.management_form }}
        {%for profile,form in profile_formset%}
          <tr>
              <td><a href="{%url 'detail_user' pk=profile.pk%}">подробнее</a></td>
            {% for field in form %}
            <td>{{ field }}</td>
            {% endfor %}
          </tr>
      {%endfor%}

        </tbody>
      </table>
      <button class="btn btn-primary btn-lg btn-block" type="submit">Сохранить изменения</button>
  </form>
    <footer class="pt-4 my-md-5 pt-md-5 border-top">
  </footer>
</div>
{%endblock%}
