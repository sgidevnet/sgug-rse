Name:           python-django
%global         pkgname Django
%global         ver 3.0.7
#global         pre ...
%global         real_version %{ver}%{?pre:%{pre}}
Version:        %{ver}%{?pre:~%{pre}}
Release:        2%{?dist}
Summary:        A high-level Python Web framework

License:        BSD
URL:            https://www.djangoproject.com/
Source0:        %{pypi_source %{pkgname} %{real_version}}

# skip tests requiring network connectivity
Patch000:       Django-2.0-skip-net-tests.patch

BuildArch:      noarch

%global _description %{expand:
Django is a high-level Python Web framework that encourages rapid
development and a clean, pragmatic design. It focuses on automating as
much as possible and adhering to the DRY (Don't Repeat Yourself)
principle.}

%description %_description


%package bash-completion
Summary:        Bash completion files for Django
BuildRequires:  bash-completion
Requires:       bash-completion

%description bash-completion
This package contains the Bash completion files form Django high-level
Python Web framework.


%package -n python3-django-doc
Summary:        Documentation for Django
%{?python_provide:%python_provide python3-django-doc}
Suggests:       python3-django = %{version}-%{release}
BuildRequires:  python3-sphinx
BuildRequires:  python3-psycopg2

%description -n python3-django-doc
This package contains the documentation for the Django high-level
Python Web framework.


%package -n python3-django
Summary:        A high-level Python Web framework
%{?python_provide:%python_provide python3-django}

Recommends:     (%{name}-bash-completion = %{version}-%{release} if bash)

BuildRequires:  python3-devel
BuildRequires:  python3-bcrypt
# test requirements
#BuildRequires: python3-py-bcrypt
BuildRequires:  python3-asgiref >= 3.2
BuildRequires:  python3-docutils
BuildRequires:  python3-jinja2
BuildRequires:  python3-mock
BuildRequires:  python3-numpy
BuildRequires:  python3-pillow
BuildRequires:  python3-PyYAML
BuildRequires:  python3-pytz
BuildRequires:  python3-selenium
BuildRequires:  python3-setuptools
BuildRequires:  python3-sqlparse >= 0.2.2
BuildRequires:  python3-memcached

Provides: bundled(jquery) = 2.2.3
Provides: bundled(xregexp) = 2.0.0

%description -n python3-django %_description

%prep
%autosetup -p1 -n %{pkgname}-%{real_version}

# hard-code python3 in django-admin
pushd django
for file in bin/django-admin.py conf/project_template/manage.py-tpl ; do
    sed -i "s/\/env python/\/python3/" $file ;
done
popd

# Python RPM dependency generator doesn't support ~= yet
# https://bugzilla.redhat.com/show_bug.cgi?id=1758141
sed -i 's/asgiref ~= /asgiref >= /' setup.py


%build
%py3_build


%install
%py3_install

%find_lang django
%find_lang djangojs
# append djangojs.lang to django.lang
cat djangojs.lang >> django.lang


# build documentation
(cd docs && mkdir djangohtml && mkdir -p _build/{doctrees,html} && make html)
cp -ar docs ..

# install man pages (for the main executable only)
mkdir -p %{buildroot}%{_mandir}/man1/
cp -p docs/man/* %{buildroot}%{_mandir}/man1/

# install bash completion script
bashcompdir=$(pkg-config --variable=completionsdir bash-completion)
mkdir -p %{buildroot}$bashcompdir
install -m 0644 -p extras/django_bash_completion \
  %{buildroot}$bashcompdir/django-admin.py

for file in django-admin django-admin-3 django-admin-%{python3_version} python3-django-admin manage.py ; do
   ln -s django-admin.py %{buildroot}$bashcompdir/$file
done

# Add backward compatible links to %%{_bindir}
ln -s ./django-admin %{buildroot}%{_bindir}/django-admin-3
ln -s ./django-admin %{buildroot}%{_bindir}/django-admin-%{python3_version}
ln -s ./django-admin %{buildroot}%{_bindir}/python3-django-admin

# remove .po files
find $RPM_BUILD_ROOT -name "*.po" | xargs rm -f

%check
cd %{_builddir}/%{pkgname}-%{real_version}
export PYTHONPATH=$(pwd)
cd tests

%{__python3} runtests.py --settings=test_sqlite --verbosity=2 --parallel 1


%files bash-completion
%{_datadir}/bash-completion

%files -n python3-django-doc
%doc docs/_build/html/*

%files -n python3-django -f django.lang
%doc AUTHORS README.rst
%license LICENSE
%{_bindir}/django-admin.py
%{_bindir}/django-admin
%{_bindir}/django-admin-3
%{_bindir}/django-admin-%{python3_version}
%{_bindir}/python3-django-admin
%{_mandir}/man1/django-admin.1*
%attr(0755,root,root) %{python3_sitelib}/django/bin/django-admin.py*
# Include everything but the locale data ...
%dir %{python3_sitelib}/django
%dir %{python3_sitelib}/django/bin
%{python3_sitelib}/django/apps
%{python3_sitelib}/django/db/
%{python3_sitelib}/django/*.py*
%{python3_sitelib}/django/utils/
%{python3_sitelib}/django/dispatch/
%{python3_sitelib}/django/template/
%{python3_sitelib}/django/urls/
%{python3_sitelib}/django/views/
%dir %{python3_sitelib}/django/conf/
%dir %{python3_sitelib}/django/conf/locale/
%dir %{python3_sitelib}/django/conf/locale/??/
%dir %{python3_sitelib}/django/conf/locale/???/
%dir %{python3_sitelib}/django/conf/locale/??_*/
%dir %{python3_sitelib}/django/conf/locale/*/LC_MESSAGES
%dir %{python3_sitelib}/django/contrib/
%{python3_sitelib}/django/contrib/*.py*
%dir %{python3_sitelib}/django/contrib/admin/
%dir %{python3_sitelib}/django/contrib/admin/locale
%dir %{python3_sitelib}/django/contrib/admin/locale/??/
%dir %{python3_sitelib}/django/contrib/admin/locale/???/
%dir %{python3_sitelib}/django/contrib/admin/locale/??_*/
%dir %{python3_sitelib}/django/contrib/admin/locale/*/LC_MESSAGES
%{python3_sitelib}/django/contrib/admin/*.py*
%{python3_sitelib}/django/contrib/admin/migrations
%{python3_sitelib}/django/contrib/admin/views/
%{python3_sitelib}/django/contrib/admin/static/
%{python3_sitelib}/django/contrib/admin/templatetags/
%{python3_sitelib}/django/contrib/admin/templates/
%dir %{python3_sitelib}/django/contrib/admindocs/
%dir %{python3_sitelib}/django/contrib/admindocs/locale/
%dir %{python3_sitelib}/django/contrib/admindocs/locale/??/
%dir %{python3_sitelib}/django/contrib/admindocs/locale/???/
%dir %{python3_sitelib}/django/contrib/admindocs/locale/??_*/
%dir %{python3_sitelib}/django/contrib/admindocs/locale/*/LC_MESSAGES
%{python3_sitelib}/django/contrib/admindocs/*.py*
%{python3_sitelib}/django/contrib/admindocs/templates/
%dir %{python3_sitelib}/django/contrib/auth/
%dir %{python3_sitelib}/django/contrib/auth/locale/
%dir %{python3_sitelib}/django/contrib/auth/locale/??/
%dir %{python3_sitelib}/django/contrib/auth/locale/???/
%dir %{python3_sitelib}/django/contrib/auth/locale/??_*/
%dir %{python3_sitelib}/django/contrib/auth/locale/*/LC_MESSAGES
%{python3_sitelib}/django/contrib/auth/*.py*
%{python3_sitelib}/django/contrib/auth/common-passwords.txt.gz
%{python3_sitelib}/django/contrib/auth/handlers/
%{python3_sitelib}/django/contrib/auth/management/
%{python3_sitelib}/django/contrib/auth/migrations/
%{python3_sitelib}/django/contrib/auth/templates/
%dir %{python3_sitelib}/django/contrib/contenttypes/
%dir %{python3_sitelib}/django/contrib/contenttypes/locale
%dir %{python3_sitelib}/django/contrib/contenttypes/locale/??/
%dir %{python3_sitelib}/django/contrib/contenttypes/locale/???/
%dir %{python3_sitelib}/django/contrib/contenttypes/locale/??_*/
%dir %{python3_sitelib}/django/contrib/contenttypes/locale/*/LC_MESSAGES
%{python3_sitelib}/django/contrib/contenttypes/*.py*
%{python3_sitelib}/django/contrib/contenttypes/__pycache__
%{python3_sitelib}/django/contrib/contenttypes/management/
%{python3_sitelib}/django/contrib/contenttypes/migrations/
%dir %{python3_sitelib}/django/contrib/flatpages/
%dir %{python3_sitelib}/django/contrib/flatpages/locale/
%dir %{python3_sitelib}/django/contrib/flatpages/locale/??/
%dir %{python3_sitelib}/django/contrib/flatpages/locale/???/
%dir %{python3_sitelib}/django/contrib/flatpages/locale/??_*/
%dir %{python3_sitelib}/django/contrib/flatpages/locale/*/LC_MESSAGES
%{python3_sitelib}/django/contrib/flatpages/*.py*
%{python3_sitelib}/django/contrib/flatpages/migrations
%{python3_sitelib}/django/contrib/flatpages/templatetags
%dir %{python3_sitelib}/django/contrib/gis/
%dir %{python3_sitelib}/django/contrib/gis/locale/
%dir %{python3_sitelib}/django/contrib/gis/locale/??/
%dir %{python3_sitelib}/django/contrib/gis/locale/???/
%dir %{python3_sitelib}/django/contrib/gis/locale/??_*/
%dir %{python3_sitelib}/django/contrib/gis/locale/*/LC_MESSAGES
%{python3_sitelib}/django/contrib/gis/*.py*
%{python3_sitelib}/django/contrib/gis/geoip2/
%{python3_sitelib}/django/contrib/gis/serializers/
%{python3_sitelib}/django/contrib/gis/static/
%dir %{python3_sitelib}/django/contrib/humanize/
%dir %{python3_sitelib}/django/contrib/humanize/locale/
%dir %{python3_sitelib}/django/contrib/humanize/locale/??/
%dir %{python3_sitelib}/django/contrib/humanize/locale/???/
%dir %{python3_sitelib}/django/contrib/humanize/locale/??_*/
%dir %{python3_sitelib}/django/contrib/humanize/locale/*/LC_MESSAGES
%{python3_sitelib}/django/contrib/humanize/templatetags/
%{python3_sitelib}/django/contrib/humanize/*.py*
%dir %{python3_sitelib}/django/contrib/messages/
%{python3_sitelib}/django/contrib/messages/*.py*
%dir %{python3_sitelib}/django/contrib/postgres
%{python3_sitelib}/django/contrib/postgres/*.py*
%{python3_sitelib}/django/contrib/postgres/aggregates
%{python3_sitelib}/django/contrib/postgres/jinja2
%{python3_sitelib}/django/contrib/postgres/fields
%{python3_sitelib}/django/contrib/postgres/forms
%{python3_sitelib}/django/contrib/postgres/templates
%{python3_sitelib}/django/contrib/postgres/__pycache__
%dir %{python3_sitelib}/django/contrib/redirects
%dir %{python3_sitelib}/django/contrib/redirects/locale
%dir %{python3_sitelib}/django/contrib/redirects/locale/??/
%dir %{python3_sitelib}/django/contrib/redirects/locale/???/
%dir %{python3_sitelib}/django/contrib/redirects/locale/??_*/
%dir %{python3_sitelib}/django/contrib/redirects/locale/*/LC_MESSAGES
%{python3_sitelib}/django/contrib/redirects/*.py*
%{python3_sitelib}/django/contrib/redirects/migrations
%dir %{python3_sitelib}/django/contrib/sessions/
%dir %{python3_sitelib}/django/contrib/sessions/locale/
%dir %{python3_sitelib}/django/contrib/sessions/locale/??/
%dir %{python3_sitelib}/django/contrib/sessions/locale/???/
%dir %{python3_sitelib}/django/contrib/sessions/locale/??_*/
%dir %{python3_sitelib}/django/contrib/sessions/locale/*/LC_MESSAGES
%{python3_sitelib}/django/contrib/sessions/management/
%{python3_sitelib}/django/contrib/sessions/migrations/
%{python3_sitelib}/django/contrib/sessions/*.py*
%{python3_sitelib}/django/contrib/sitemaps/
%dir %{python3_sitelib}/django/contrib/sites/
%dir %{python3_sitelib}/django/contrib/sites/locale/
%dir %{python3_sitelib}/django/contrib/sites/locale/??/
%dir %{python3_sitelib}/django/contrib/sites/locale/???/
%dir %{python3_sitelib}/django/contrib/sites/locale/??_*/
%dir %{python3_sitelib}/django/contrib/sites/locale/*/LC_MESSAGES
%{python3_sitelib}/django/contrib/sites/*.py*
%{python3_sitelib}/django/contrib/sites/migrations
%{python3_sitelib}/django/contrib/staticfiles/
%{python3_sitelib}/django/contrib/syndication/
%{python3_sitelib}/django/contrib/gis/admin/
%{python3_sitelib}/django/contrib/gis/db/
%{python3_sitelib}/django/contrib/gis/forms/
%{python3_sitelib}/django/contrib/gis/gdal/
%{python3_sitelib}/django/contrib/gis/geos/
%{python3_sitelib}/django/contrib/gis/management/
%{python3_sitelib}/django/contrib/gis/sitemaps/
%{python3_sitelib}/django/contrib/gis/templates/
%{python3_sitelib}/django/contrib/gis/utils/
%{python3_sitelib}/django/contrib/messages/storage/
%{python3_sitelib}/django/contrib/sessions/backends/
%{python3_sitelib}/django/forms/
%{python3_sitelib}/django/templatetags/
%{python3_sitelib}/django/core/
%{python3_sitelib}/django/http/
%{python3_sitelib}/django/middleware/
%{python3_sitelib}/django/test/
%{python3_sitelib}/django/conf/*.py*
%{python3_sitelib}/django/conf/project_template/
%{python3_sitelib}/django/conf/app_template/
%{python3_sitelib}/django/conf/urls/
%{python3_sitelib}/django/conf/locale/*/*.py*
%{python3_sitelib}/django/conf/locale/*.py*
%{python3_sitelib}/%{pkgname}-%{real_version}-py%{python3_version}.egg-info
%{python3_sitelib}/django/__pycache__
%{python3_sitelib}/django/bin/__pycache__
%{python3_sitelib}/django/conf/__pycache__
%{python3_sitelib}/django/conf/locale/*/__pycache__
%{python3_sitelib}/django/contrib/__pycache__
%{python3_sitelib}/django/contrib/admin/__pycache__
%{python3_sitelib}/django/contrib/admindocs/__pycache__
%{python3_sitelib}/django/contrib/auth/__pycache__
%{python3_sitelib}/django/contrib/flatpages/__pycache__
%{python3_sitelib}/django/contrib/gis/__pycache__
%{python3_sitelib}/django/contrib/humanize/__pycache__
%{python3_sitelib}/django/contrib/messages/__pycache__
%{python3_sitelib}/django/contrib/redirects/__pycache__
%{python3_sitelib}/django/contrib/sessions/__pycache__
%{python3_sitelib}/django/contrib/sites/__pycache__


%changelog
* Wed Jun 24 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 3.0.7-2
- Add BR on setuptools

* Sun Jun 07 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.7-1
- Update to 3.0.7
- Security fix for CVE-2020-7471 (rhbz#1798516)
- Security fix for CVE-2020-9402 (rhbz#1810093)
- Security fix for CVE-2020-13254 (rhbz#1843617)
- Security fix for CVE-2020-13596 (rhbz#1843627)

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Matthias Runge <mrunge@redhat.com> - 3.0.2-1
- bugfix release

* Tue Dec 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0-1
- Update to 3.0 final

* Tue Oct 15 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0~b1-1
- Update to 3.0b1 (rhbz#1761417)

* Fri Oct 04 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0~a1-1
- Update to 3.0a1 (rhbz#1750709)
- https://fedoraproject.org/wiki/Changes/Django3

* Thu Sep 05 2019 Matthias Runge <mrunge@redhat.com> - 2.2.5-1
- bugfix release 2.2.5 (rhbz#1747876)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.4-2
- Rebuilt for Python 3.8

* Tue Aug 06 2019 Matthias Runge <mrunge@redhat.com> - 2.2.4-1
- fix CVE-2019-14235 (rhbz#1735784)
- fix CVE-2019-14234 (rhbz#1735780)
- fix CVE-2019-14233 (rhbz#1735775)
- fix CVE-2019-14232 (rhbz#1735771)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 04 2019 Matthias Runge <mrunge@redhat.com> - 2.2.3-1
- fix CVE-2019-12781 Incorrect HTTP detection with reverse-proxy connecting
  via HTTPS (rhbz#1726014)

* Tue Jun 04 2019 Matthias Runge <mrunge@redhat.com> - 2.2.2-1
- fix CVE-2019-12308 AdminURLFieldWidget XSS
  (rhbz#1716763)

* Wed Apr 10 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2-1
- Update to 2.2 (rhbz#1674439)

* Wed Feb 20 2019 Matthias Runge <mrunge@redhat.com> - 2.1.7-1
- Fix CVE-2019-6975: Memory exhaustion in django.utils.numberformat.format()
  rhbz#1678264

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.5-2
- Enable python dependency generator

* Mon Jan 07 2019 Matthias Runge <mrunge@redhat.com> - 2.1.5-1
- fix CVE-2019-3498 python-django: Content spoofing via URL path in
  default 404 page (rhbz#1663723)

* Mon Oct 22 2018 Matthias Runge <mrunge@redhat.com> - 2.1.2-1
- fix CVE-2018-16984 Password hash disclosure to “view only” admin users
  (rhbz#1639399)

* Fri Aug 17 2018 Matthias Runge <mrunge@redhat.com> - 2.1-1
- update to 2.1 (rhbz#1611025)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Matthias Runge <mrunge@redhat.com> - 2.0.7-1
- bugfix update to 2.0.7 (rhbz#1597265)

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.6-2
- Rebuilt for Python 3.7

* Mon Jun 04 2018 Matthias Runge <mrunge@redhat.com> - 2.0.6-1
- bugfix update to 2.0.6 (rhbz#1585347)

* Thu May 03 2018 Matthias Runge <mrunge@redhat.com> - 2.0.5-1
- update to 2.0.5 (rhbz#1574123)

* Tue Apr 03 2018 Matthias Runge <mrunge@redhat.com> - 2.0.4-1
- update to 2.0.4 (rhbz#1541188)

* Fri Mar 16 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-4
- Obsolete pythonX-django-ckeditor, pythonX-django-extensions,
  pythonX-django-helpdesk, pythonX-django-openid-auth, pythonX-django-pylibmc,
  pythonX-django-select2, pythonX-django-setuptest,
  pythonX-django-federated-login

* Sun Mar 11 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-3
- Obsolete pythonX-django-pgjson

* Wed Mar 07 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-2
- Obsolete pythonX-django-sekizai and pythonX-django-south

* Tue Mar 06 2018 Matthias Runge <mrunge@redhat.com> - 2.0.3-1
- update to 2.0.3, fix CVE-2018-7536 (rhbz#1552178)

* Fri Mar 02 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-4
- Obsolete packages retired from https://pagure.io/fesco/issue/1857

* Fri Mar 02 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-3
- Obsolete pythonX-django-model-utils and pythonX-django-netjsongraph

* Wed Feb 07 2018 Matthias Runge <mrunge@redhat.com> - 2.0.2-2
- requires python2 while being python3 (rhbz#15424)

* Fri Feb 02 2018 Matthias Runge <mrunge@redhat.com> - 2.0.2-1
- fix CVE-2018-6188

* Tue Jan 16 2018 Matthias Runge <mrunge@redhat.com> - 2.0.1-1
- update to 2.0.1
- remove python2 bits
- enable python3 tests

* Tue Jan 16 2018 Troy Dawson <tdawson@redhat.com> - 1.11.9-2
- Update conditionals

* Thu Jan 04 2018 Miro Hrončok <mhroncok@redhat.com> - 1.11.9-1
- update to 1.11.9

* Thu Jan 04 2018 Miro Hrončok <mhroncok@redhat.com> - 1.11.8-2
- Obsolete python(2)-django-devserver

* Fri Dec 15 2017 Matthias Runge <mrunge@redhat.com> - 1.11.8-1
- update to 1.11.8

* Wed Sep 06 2017 Matthias Runge <mrunge@redhat.com> - 1.11.5-1
- update to 1.11.5 (rhbz#1488683)

* Wed Aug 02 2017 Matthias Runge <mrunge@redhat.com> - 1.11.4-1
- update to 1.11.4 (rhbz#1477382)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Matthias Runge <mrunge@redhat.com> - 1.11.3-1
- Update to 1.11.3 (rhbz#1467029)

* Thu Jun 15 2017 Matthias Runge <mrunge@redhat.com> - 1.11.2-1
- update to 1.11.2 (rhbz#1448664
- add dependency to pytz (rhbz#1458493)

* Thu Apr 06 2017 Matthias Runge <mrunge@redhat.com> - 1.11-1
- update to 1.11 (rhbz#1410268)

* Tue Feb 28 2017 Matthias Runge <mrunge@redhat.com> - 1.10.5-1
- rebase to 1.10.5, fix FTBFS (rhbz#1424135)
- declare bundled libs (rhbz#1401243)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 Stratakis Charalampos <cstratak@redhat.com> - 1.10.4-2
- Rebuild for Python 3.6
- Disable python3 tests for now

* Fri Dec 02 2016 Matthias Runge <mrunge@redhat.com> - 1.10.4-1
- update to stable 1.10.4 (rhbz#1400730)

* Wed Nov 02 2016 Matthias Runge <mrunge@redhat.com> - 1.10.3-1
- update to 1.10.3 (rhbz#1390782)
- fix CVE-2016-9013, CVE-2016-9014

* Mon Oct 03 2016 Matthias Runge <mrunge@redhat.com> - 1.10.2-1
- update to 1.10.2 (rhbz#1381019)

* Thu Sep 22 2016 Matthias Runge <mrunge@redhat.com> - 1.10.1-1
- rebase to 1.10.1 (rhbz#1338391)

* Thu Jul 21 2016 Matthias Runge <mrunge@redhat.com> - 1-9.8-1
- fix CVE-2016-6186 (rhbz#1357701)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.7-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jun 06 2016 Matthias Runge <mrunge@redhat.com> - 1.9.7-1
- bugfix release

* Tue May 31 2016 Nils Philippsen <nils@redhat.com>
- fix source URL

* Sun May  8 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.9.6-2
- Put the provives/obsoletes in the right spot for new python naming

* Tue May 03 2016 Matthias Runge <mrunge@redhat.com> - 1.9.6-1
- update to 1.9.6 (rhbz#1323374)

* Tue Mar 08 2016 Matthias Runge <mrunge@redhat.com> - 1.9.4-1
- update to 1.9.4 fixing a regression introduced in last
  upstream fix for CVE-2016-2512

* Wed Mar 02 2016 Matthias Runge <mrunge@redhat.com> - 1.9.3-1
- update to 1.9.3, fixing CVE-2016-2512, CVE-2016-2513
  (rhbz#1313500)

* Thu Feb 11 2016 Matthias Runge <mrunge@redhat.com> - 1.9.2-1
- update to 1.9.2 (rhbz#1266062)
- modernize spec file, provide py2, obsolete python-django

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

