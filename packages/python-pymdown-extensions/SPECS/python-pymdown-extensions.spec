# Created by pyp2rpm-3.3.0
%global pypi_name pymdown-extensions

Name:           python-%{pypi_name}
Version:        7.0
Release:        2%{?dist}
Summary:        Extension pack for Python Markdown

# Most of the package is MIT, three files (extrarawhtml.py, highlight.py and
# superfences.py are BSD
License:        MIT and BSD
URL:            https://facelessuser.github.io/pymdown-extensions/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%description
PyMdown Extensions (pymdownx) is a collection of extensions for Python
Markdown.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3dist(markdown)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3-pyyaml
BuildRequires:  python3-pytest

%description -n python3-%{pypi_name}
PyMdown Extensions (pymdownx) is a collection of extensions for Python
Markdown.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py3_build


%install
%py3_install


%check
%{__python3} run_tests.py


%files -n python3-%{pypi_name}
%license LICENSE.md
%doc README.md
%{python3_sitelib}/pymdownx
%{python3_sitelib}/pymdown_extensions-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 7.0-2
- Rebuilt for Python 3.9

* Wed Apr  8 2020 Robin Lee <cheeselee@fedoraproject.org> - 7.0-1
- Update to 7.0

* Thu Mar 12 2020 Robin Lee <cheeselee@fedoraproject.org> - 6.3-2
- Bump release for koji error:
  https://pagure.io/fedora-infrastructure/issue/8738

* Sun Mar  8 2020 Robin Lee <cheeselee@fedoraproject.org> - 6.3-1
- Update to 6.3

* Wed Apr 11 2018 Stephen Gallagher <sgallagh@redhat.com> - 3.5-4
- Update license information

* Wed Apr 04 2018 Stephen Gallagher <sgallagh@redhat.com> - 3.5-1
- Initial package.
