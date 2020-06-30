%global pypi_name Events
%global _description\
Bringing the elegance of C EventHandler to Python The C language provides a\
handy way to declare, subscribe to and fire events. Technically, an event is a\
"slot" where callback functions (event handlers) can be attached to a process\
referred to as subscribing to an event. Here is a handy package that\
encapsulates the core to event subscription and event firing and feels like a\
"natural" ...

Name:           python-events
Version:        0.3
Release:        9%{?dist}
Summary:        Bringing the elegance of C# EventHandler to Python

License:        BSD

URL:            http://github.com/pyeve/events
Source0:        https://pypi.org/packages/source/E/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%description    %_description

%package -n     python3-events
Summary:        %{summary}
%{?python_provide:%python_provide python3-events}

%description -n python3-events %_description

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install


%check
%{__python3} setup.py test

%files -n python3-events
%license LICENSE
%doc README.rst
%{python3_sitelib}/events
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3-3
- Subpackage python2-events has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 24 2018 Carl George <carl@george.computer> - 0.3-1
- Latest upstream

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-4
- Rebuilt for Python 3.7

* Sun Apr 08 2018 David Hannequin <david.hannequin@gmail.com> - 0.2.1-3
- Fix bug 1508962..

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 08 2017 David Hannequin <david.hannequin@gmail.com> - 0.2.1-1
- Initial package.
