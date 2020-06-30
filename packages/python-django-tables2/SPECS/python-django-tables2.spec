%global srcname django-tables2

Name:           python-django-tables2
Version:        2.1.0
Release:        3%{?dist}
Summary:        Table framework for Django

License:        BSD
URL:            https://github.com/jieter/django-tables2
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
django-tables2 simplifies the task of turning sets of data into HTML tables.
It has native support for pagination and sorting. It does for HTML tables
what django.forms does for HTML forms.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Obsoletes:      python-%{srcname} < 1.2.3-5
Obsoletes:      python2-%{srcname} < 1.2.3-5

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version}
rm -vr *.egg-info/

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.md CHANGELOG.md
%{python3_sitelib}/django_tables2/
%{python3_sitelib}/django_tables2-*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 31 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.17.1-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.17.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Matthias Runge <mrunge@redhat.com> - 1.17.1-1
- rebase to 1.17.1

* Wed Jan 17 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.3-5
- Remove Python 2 subpackage for https://fedoraproject.org/wiki/Changes/Django20

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.3-2
- Rebuild for Python 3.6

* Wed Aug 31 2016 Lumir Balhar <lbalhar@redhat.com> - 1.2.3-2
- Added condition to allow Python3 subpackage only in Fedora

* Tue Jul 26 2016 Dominika Krejci <dkrejci@redhat.com> - 1.2.3-1
- Update to 1.2.3
- Make Python 3 work

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 22 2016 Matthias Runge <mrunge@redhat.com> - 1.1.2-1
- update to 1.1.2
- add python2, python3 subpackge

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 16 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.10.0-1
* Wed Mar 07 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.9.4-2
- remove included egg-info
- more specific %%files-section

* Sat Mar 03 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.9.4-1
- initial packaging
