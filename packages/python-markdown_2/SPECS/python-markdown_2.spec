%global pypi_name Markdown
%global modname markdown

Name:           python-%{modname}_2
Version:        2.6.11
Release:        2%{?dist}
Summary:        Python implementation of Markdown

License:        BSD
URL:            https://github.com/Python-Markdown/markdown
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
%{summary}.}

%description %{_description}

%package     -n python3-%{modname}_2
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
Conflicts:      python%{python3_version}dist(%{modname})

%description -n python3-%{modname}_2 %{_description}

Python 3 version.

%prep
%autosetup -n %{pypi_name}-%{version} -p1
rm -vr *.egg-info
sed -i -e '/markdown.__main__/d' setup.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{modname}_2
%license LICENSE.md
%doc README.md
%{python3_sitelib}/markdown/
%{python3_sitelib}/Markdown-*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.6.11-2
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.6.11-1
- Initial package
