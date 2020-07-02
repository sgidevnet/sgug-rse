%global srcname django-cors-headers

Name:           python-%{srcname}
Version:        3.1.0
Release:        3%{?dist}
Summary:        Django application for handling the server headers required for CORS

License:        MIT
URL:            https://github.com/adamchainz/django-cors-headers
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
A Django App that adds Cross-Origin Resource Sharing (CORS) headers
to responses. This allows in-browser requests to your Django application
from other origins.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -vrf *.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst HISTORY.rst
%{python3_sitelib}/django_cors_headers-*.egg-info/
%{python3_sitelib}/corsheaders/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 31 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-7
- Rebuilt for Python 3.7

* Tue Mar 06 2018 Ralph Bean <rbean@redhat.com> - 2.0.2-6
- Make py3 package provide the old py2 name.

* Mon Mar 05 2018 Ralph Bean <rbean@redhat.com> - 2.0.2-5
- Disable python2 for https://fedoraproject.org/wiki/Changes/Django20

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 28 2017 Ralph Bean <rbean@redhat.com> - 2.0.2-2
- Add missing doc and license declarations.

* Fri Feb 10 2017 Ralph Bean <rbean@redhat.com> - 2.0.2-1
- Latest upstream.

* Mon Jan 18 2016 Ralph Bean <rbean@redhat.com> - 1.1.0-2
- Initial packaging for Fedora.
