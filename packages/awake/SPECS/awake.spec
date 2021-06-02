Name:           awake
Version:        1.0
Release:        18%{?dist}
Summary:        A command to 'wake on LAN' a remote host

License:        GPLv3
URL:            https://github.com/cyraxjoe/awake
Source0:        https://github.com/cyraxjoe/awake/archive/v%{version}.zip
BuildArch:      noarch

BuildRequires:  python3-devel
Requires:       python3-awake

%description
A command to 'wake on LAN' a remote host.

%package -n python3-%{name}
Summary:        Python bindings for %{name}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
Python bindings for %{name}.

%prep
%autosetup
sed -i -e '/^#!\//, 1d' *.py

%build
%py3_build

%install
%py3_install

%files -n awake
%doc CHANGES LICENSE README
%{_bindir}/%{name}

%files -n python3-%{name}
%doc CHANGES README
%license LICENSE
%{python3_sitelib}/%{name}/
%{python3_sitelib}/*.egg-info

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0-15
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0-11
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Mar 10 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.0-9
- Remove shebang

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 15 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.0-7
- Cleanup
- Fix conflict (rhbz#1269350)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri Nov 15 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.0-2
- Fix requirements (rhbz#1029247)

* Fri Mar 01 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.0-1
- Initial package
