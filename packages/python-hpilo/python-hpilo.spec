%global srcname hpilo

Name:           python-%{srcname}
Version:        4.3
Release:        2%{?dist}
Summary:        iLO automation from python or shell

License:        ASL 2.0 or GPLv3+
URL:            https://github.com/seveas/python-hpilo
Source:         %{pypi_source %{name}}

BuildArch:      noarch

%global _description \
%{summary}.

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %{_description}

Python 3 version.

%package        doc
Summary:        Documentation for %{name}
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%description    doc
%{summary}.

%prep
%autosetup

%build
%py3_build
sphinx-build -b html docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%files -n python3-%{srcname}
%license COPYING
%doc README.md CHANGES examples ilo.conf.example
%{_bindir}/hpilo_cli
%{python3_sitelib}/hpilo.py
%{python3_sitelib}/hpilo_fw.py
%{python3_sitelib}/__pycache__/hpilo*
%{python3_sitelib}/python_hpilo-*.egg-info

%files doc
%license COPYING
%doc html

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 12:36:09 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.3-1
- Initial package
