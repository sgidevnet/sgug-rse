# Created by pyp2rpm-3.2.2
%global pypi_name pyModbusTCP

Name:           python-%{pypi_name}
Version:        0.1.8
Release:        3%{?dist}
Summary:        A simple Modbus/TCP library for Python

License:        MIT
URL:            https://github.com/sourceperl/pyModbusTCP
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
pyModbusTCP A simple Modbus/TCP client library for Python.
Since version 0.1.0, a server is also available for test 
purpose only (don't use in project). pyModbusTCP is pure Python 
code without any extension or external module dependency.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
pyModbusTCP A simple Modbus/TCP client library for Python.
Since version 0.1.0, a server is also available for test 
purpose only (don't use in project). pyModbusTCP is pure Python 
code without any extension or external module dependency.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.8-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Steve Traylen <steve.traylen@cern.ch> - 0.1.8-1
- Update to 0.1.8

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1.5-7
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-5
- Rebuilt for Python 3.7

* Sun Apr 29 2018 Iryna Shcherbina <shcherbina.iryna@gmail.com> - 0.1.5-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Apr 24 2018 Steve Traylen <steve.traylen@cern.ch> - 0.1.5-3
- Correct previous wrong date

* Wed Mar 28 2018 Steve Traylen <steve.traylen@cern.ch> - 0.1.5-2
- Correct spec file name.

* Fri Jan 26 2018 Steve Traylen <steve.traylen@cern.ch> - 0.1.5-1
- Initial package.
