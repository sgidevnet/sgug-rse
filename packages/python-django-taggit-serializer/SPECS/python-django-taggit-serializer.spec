%global srcname django-taggit-serializer

Name:           python-%{srcname}
Version:        0.1.7
Release:        3%{?dist}
Summary:        Django Taggit serializer for Django REST Framework

License:        BSD
URL:            https://github.com/glemmaPaul/django-taggit-serializer
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

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.md HISTORY.rst
%{python3_sitelib}/django_taggit_serializer-*.egg-info/
%{python3_sitelib}/taggit_serializer/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 06 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.7-1
- Initial package
