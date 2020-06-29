%global pypi_name sphinx-last-updated-by-git

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        2%{?dist}
Summary:        Get the "last updated" time for each Sphinx page from Git

License:        BSD
URL:            https://github.com/mgeier/sphinx-last-updated-by-git/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Get the "last updated" time for each Sphinx page from Git. This is a little
Sphinx_ extension that does exactly that.It also checks for included files and
other dependencies.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Get the "last updated" time for each Sphinx page from Git. This is a little
Sphinx_ extension that does exactly that.It also checks for included files and
other dependencies.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/sphinx_last_updated_by_git.py
%{python3_sitelib}/sphinx_last_updated_by_git-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-2
- Rebuilt for Python 3.9

* Fri May 15 2020 Charalampos Stratakis <cstratak@redhat.com> - 0.2.1-1
- Initial package.