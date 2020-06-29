%global pypi_name click-man

Name:           python-%{pypi_name}
Version:        0.4.1
Release:        2%{?dist}
Summary:        Generate man pages for click based CLI applications

License:        MIT
URL:            https://github.com/click-contrib/click-man
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Automatically produces UNIX-style manual pages for Python applications that
use Click for option handling.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 

%description -n python3-%{pypi_name}
Automatically produces UNIX-style manual pages for Python applications that
use Click for option handling.


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
%doc README.md
%{_bindir}/click-man
%{python3_sitelib}/click_man
%{python3_sitelib}/click_man-%{version}-py?.?.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-2
- Rebuilt for Python 3.9

* Mon Apr 27 2020 Jiri Popelka <jpopelka@redhat.com> - 0.4.1-1
- 0.4.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 21 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-5
- Drop Python 2 BuildRequires

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 2019 Jiri Popelka <jpopelka@redhat.com> - 0.3.0-1
- 0.3.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 01 2018 Stephen Gallagher <sgallagh@redhat.com> - 0.2.2-5
- Drop Python2 package

* Fri Aug 31 2018 Stephen Gallagher <sgallagh@redhat.com> - 0.2.2-4
- Fix description
- Use python?dist()-style BuildRequires

* Thu Aug 30 2018 Stephen Gallagher <sgallagh@redhat.com> - 0.2.2-3
- Use automatic dependency generator

* Wed Aug 29 2018 Stephen Gallagher <sgallagh@redhat.com> - 0.2.2-2
- Add missing URL

* Wed Aug 29 2018 Stephen Gallagher <sgallagh@redhat.com> - 0.2.2-1
- Initial package.
