%global srcname django-taggit

Name:           python-%{srcname}
Version:        1.1.0
Release:        3%{?dist}
Summary:        Reusable Django application for simple tagging

License:        BSD
URL:            https://github.com/jazzband/django-taggit
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
%{summary}.}

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
rm -vr *.egg-info
# remove unnecessary language ressources:
rm taggit/locale/*/LC_MESSAGES/django.po

%build
%py3_build

%install
%py3_install
%find_lang django

%files -n python3-%{srcname} -f django.lang
%license LICENSE
%doc README.rst CHANGELOG.rst
%{python3_sitelib}/django_taggit-*.egg-info/
%{python3_sitelib}/taggit/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 06 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-1
- Initial package
