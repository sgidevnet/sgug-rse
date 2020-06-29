%global srcname django-timezone-field

Name:           python-%{srcname}
Version:        4.0
Release:        2%{?dist}
Summary:        Django app providing database and form fields for pytz timezone objects

License:        BSD
URL:            https://github.com/mfogel/django-timezone-field
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
%{summary}.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -vr *.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/django_timezone_field-*.egg-info/
%{python3_sitelib}/timezone_field/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0-2
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 4.0-1
- Update to 4.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 06 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0-1
- Initial package
