%global srcname getmac

Name:           python-%{srcname}
Version:        0.7.0
Release:        6%{?dist}
Summary:        Python module to get the MAC address of local network interfaces and LAN hosts

License:        MIT
URL:            https://github.com/GhostofGoes/getmac
Source0:        %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel, python3-setuptools

%description
Pure-python module to get the MAC address of remote hosts or network interfaces.
It provides a platform-independent interface to get the MAC addresses of network
interfaces on the local system(by interface name) and remote hosts on the local
network (by IPv4/IPv6 address or host-name).

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-getmac}

%description -n python3-%{srcname}
Pure-python module to get the MAC address of remote hosts or network interfaces.
It provides a platform-independent interface to get the MAC addresses of network
interfaces on the local system(by interface name) and remote hosts on the local
network (by IPv4/IPv6 address or host-name).

%prep
%autosetup -n %{srcname}-%{version}

%build
sed -i '1{/^#!\//d}' getmac/__main__.py
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/
/usr/bin/getmac
%{_mandir}/man1/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 13 2018 Henrik Boeving <hargonix@gmail.com> - 0.6.0-1
- initial packaging
