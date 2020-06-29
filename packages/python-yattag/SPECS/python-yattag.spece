%global pkgname yattag
%global desc Generate HTML or XML in a pythonic way

# Settings for Fedora > 29 and EL > 7
%if 0%{?fedora} > 29 || 0%{?rhel} > 7
%bcond_with                 python2
%else
%bcond_without              python2
%endif

Name:           python-%{pkgname}
Version:        1.10.0
Release:        10%{?dist}
Summary:        Pure python alternative to web template engines

License:        LGPLv2
URL:            https://pypi.python.org/pypi/yattag
Source0:        https://files.pythonhosted.org/packages/source/y/%{pkgname}/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch

%description
%{desc}

%if %{with python2}
%package -n python2-%{pkgname}
BuildRequires:  python2-devel
BuildRequires:  python2-nose
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pkgname}}

%description -n python2-%{pkgname}
%{desc}
%endif

%package -n python3-%{pkgname}
BuildRequires:  python3-devel
BuildRequires:  python3-nose
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}

%description -n python3-%{pkgname}
%{desc}

%prep
%autosetup -n %{pkgname}-%{version}

# Remove upstream egg-info
rm -rf %{pkgname}.egg-info

%build
%{?with_python2: %py2_build}
%py3_build

%install
%{?with_python2: %py2_install}
%py3_install

%check
%{?with_python2: %{__python2} -m nose -v}
%{__python3} -m nose -v

%if %{with python2}
%files -n python2-%{pkgname}
%doc README.rst
%license license/COPYING
%{python2_sitelib}/%{pkgname}-%{version}-py%{python2_version}.egg-info
%{python2_sitelib}/yattag
%endif


%files -n python3-%{pkgname}
%doc README.rst
%license license/COPYING
%{python3_sitelib}/%{pkgname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/yattag

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 26 2018 Sebastian Kisela <skisela@redhat.com> - 1.10.0-4
- python2 will be deprecated soon. Build python3 packages only.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-2
- Rebuilt for Python 3.7

* Thu Mar 22 2018 Sebastian Kisela <skisela@redhat.com> - 1.10.0-1
- New upstream release 1.10.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 08 2017 Sebastian Kisela <skisela@redhat.com> - 1.9.2-1
- New upstream release 1.9.2

* Mon Oct 09 2017 skisela@redhat.com - 1.9.0-2
- Fix description macro. Reported at https://bugzilla.redhat.com/1498071.

* Wed Aug 23 2017 Sebastian Kisela <skisela@redhat.com> - 1.9.0-1
- New upstream release 1.9.0

* Wed Jul 26 2017 Sebastian Kisela <skisela@redhat.com> - 1.8.0-1
- Initial 1.8.0 package version.

