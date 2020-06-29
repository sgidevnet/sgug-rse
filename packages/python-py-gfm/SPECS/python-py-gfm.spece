%global srcname py-gfm

Name:           python-%{srcname}
Version:        0.1.4
Release:        2%{?dist}
Summary:        Github-Flavored Markdown for Python-Markdown

License:        BSD
URL:            https://github.com/zopieux/py-gfm
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
BuildRequires:  python3dist(markdown) < 3.0

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -vr *.egg-info
sed -i -e '/data_files/d' setup.py

%build
%py3_build

%install
%py3_install

%check
%python3 -m unittest discover tests

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst CHANGELOG.md
%{python3_sitelib}/gfm/
%{python3_sitelib}/mdx_gfm/
%{python3_sitelib}/mdx_partial_gfm/
%{python3_sitelib}/py_gfm-*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.4-2
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.4-1
- Initial package
