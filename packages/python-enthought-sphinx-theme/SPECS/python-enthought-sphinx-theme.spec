%global srcname enthought-sphinx-theme
%global modname enthought_sphinx_theme

Name:           python-%{srcname}
Version:        0.6.2
Release:        1%{?dist}
Summary:        Sphinx theme for Enthought projects

# Bundled bootstrap is MIT
# Bundles the fonts Source Sans Pro and Source Code Pro from Adobe Systems Incorporated under the 
# SIL Open Font License, Version 1.1.
License:        BSD and MIT and OFL
URL:            https://github.com/enthought/enthought-sphinx-theme
Source0:        https://github.com/enthought/enthought-sphinx-theme/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
Sphinx theme for Enthought projects, derived from the Scipy theme.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}
Provides:       bundled(bootstrap) = 2.3.2

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

#check
# No tests

%files -n python3-%{srcname}
%license LICENSE licenses/*.txt
%doc CHANGES.rst README.rst
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}/

%changelog
* Wed Jun 24 2020 Orion Poplawski <orion@nwra.com> - 0.6.2-1
- Update to 0.6.2
- Add BR on python-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 5 2019 Orion Poplawski <orion@nwra.com> - 0.6.1-2
- Fix licensing
- Drop bogus %%check

* Tue Oct 1 2019 Orion Poplawski <orion@nwra.com> - 0.6.1-1
- Initial package
