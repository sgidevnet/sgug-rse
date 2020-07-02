%global srcname batinfo

Name:           python-%{srcname}
Version:        0.4.2
Release:        16%{?dist}
Summary:        Python module to retrieve battery information

License:        LGPLv3+
URL:            https://github.com/nicolargo/batinfo
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
Buildarch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
A simple Python module to retrieve battery information on Linux-based
operating system. No ACPI or external software is needed. Only the Linux
kernel and its /sys/class/power_supply folder.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A simple Python module to retrieve battery information on Linux-based
operating system. No ACPI or external software is needed. Only the Linux
kernel and its /sys/class/power_supply folder.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install
rm -rf %{buildroot}%{_defaultdocdir}/%{srcname}/

%files -n python3-%{srcname}
%doc AUTHORS README.md
%license LICENSE
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.2-10
- Subpackage python2-batinfo has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-8
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.2-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.2-5
- Enable Python3 support by default

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-3
- Rebuild for Python 3.6

* Mon Nov 21 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.2-2
- Update description

* Fri Nov 18 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.2-1
- Add license and remove shebang removal
- Update to latest upstream release 0.4.2

* Tue Nov 15 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.3-1
- Initial package
