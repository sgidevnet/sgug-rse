# what it's called on pypi
%global srcname prompt_toolkit
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname prompt-toolkit

%global common_description %{expand:
prompt_toolkit is a library for building powerful interactive command lines and
terminal applications in Python.}

%bcond_without tests


Name:           python-%{pkgname}
Version:        3.0.5
Release:        3%{?dist}
Summary:        Library for building powerful interactive command lines in Python
License:        BSD
URL:            https://github.com/prompt-toolkit/python-prompt-toolkit
Source0:        %pypi_source
BuildArch:      noarch


%description %{common_description}


%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
%if %{with tests}
BuildRequires:  %{py3_dist pytest wcwidth}
%endif
# https://github.com/jonathanslenders/python-prompt-toolkit/issues/94
Recommends:     %{py3_dist pygments}
# renamed from python3-prompt_toolkit
Obsoletes:      python3-prompt_toolkit < 1.0.16-2
Provides:       python3-prompt_toolkit = %{version}-%{release}
%{?python_provide:%python_provide python3-%{pkgname}}


%description -n python3-%{pkgname} %{common_description}


%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{eggname}.egg-info


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} --verbose
%endif


%files -n python3-%{pkgname}
%doc README.rst AUTHORS.rst CHANGELOG
%license LICENSE
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info


%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.5-3
- Rebuilt for Python 3.9

* Thu May 14 2020 Carl George <carl@george.computer> - 3.0.5-2
- Remove six dependency

* Tue May 05 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.0.5-1
- Latest upstream

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 17 2019 Carl George <carl@george.computer> - 2.0.10-1
- Latest upstream

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.9-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.9-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Carl George <carl@george.computer> - 2.0.9-2
- Increase obsoletes version for upgrade path rhbz#1700292

* Wed Mar 20 2019 Carl George <carl@george.computer> - 2.0.9-1
- Latest upstream

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 06 2018 Carl George <carl@george.computer> - 2.0.7-1
- Latest upstream rhbz#1647178

* Mon Oct 01 2018 Carl George <carl@george.computer> - 2.0.5-1
- Latest upstream
- Remove python2 subpackage

* Fri Sep 28 2018 Carl George <carl@george.computer> - 2.0.4-1
- Latest upstream
- Rename from *-prompt_toolkit to *-prompt-toolkit

* Fri Sep 28 2018 Carl George <carl@george.computer> - 1.0.15-2
- Revert using a common documentation directory to avoid potential update issues
- Change pygments to an optional dependency

* Thu Jul 12 2018 Carl George <carl@george.computer> - 1.0.15-1
- Latest upstream
- Use common documentation directory

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.14-6
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Carl George <carl@george.computer> - 1.0.14-5
- Make requirements compatible with EPEL
- Build for Python 3 in EPEL
- Run test suite
- Remove duplicate provides

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.14-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 01 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.0.14-1
- Update to 1.0.14

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.9-2
- Rebuild for Python 3.6

* Sun Dec 11 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.0.9-1
- Update to 1.0.9

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri May 06 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Tue Mar 29 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.60-1
- Update to 0.60

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.57-2
- Make the EL6 package provide python-prompt_toolkit too

* Sat Jan 09 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.57-1
- New upstream update

* Wed Jan 06 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.54-2
- Fix quiet setup
- Fix license
- Add AUTHORS.rst, CHANGELOG & TODO.rst

* Tue Dec 29 2015 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.54-1
- Initial package.
