# Created by pyp2rpm-3.3.2
%global pypi_name pysol-cards

Name:           python-%{pypi_name}
Version:        0.10.1
Release:        1%{?dist}
Summary:        Deal PySol FC Cards
License:        MIT
URL:            https://fc-solve.shlomifish.org/
Source0:        %{pypi_source pysol_cards}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pbr >= 2
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-six

%description
The pysol-cards python module allows the python developer to generate the
initial deals of some PySol FC games.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
The pysol-cards python module allows the python developer to generate the
initial deals of some PySol FC games.

%prep
%autosetup -n pysol_cards-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
sed -i '/^#! \/usr\/bin\/env python$/d' pysol_cards/*.py

%build
%py3_build

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst doc/source/readme.rst
%{python3_sitelib}/pysol_cards
%{python3_sitelib}/pysol_cards-%{version}-py?.?.egg-info

%changelog
* Sun Jun 14 2020 Shlomi Fish <shlomif@shlomifish.org> 0.10.1-1
- Update to the new upstream version.

* Sat May 30 2020 Shlomi Fish <shlomif@shlomifish.org> 0.8.18-1
- Update to the new upstream version.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.9-4
- Rebuilt for Python 3.9

* Mon May 18 2020 Sérgio Basto <sergio@serjux.com> - 0.8.9-3
- Fix build on EPEL7

* Sat Mar 28 2020 Shlomi Fish <shlomif@cpan.org> 0.8.9-2
- Correct the date in the changelog.

* Sat Mar 28 2020 Shlomi Fish <shlomif@cpan.org> 0.8.9-1
- New upstream release.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.6-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.6-2
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Shlomi Fish <shlomif@cpan.org> 0.4.1-1
- Initial Fedora package based on the Mageia one.
