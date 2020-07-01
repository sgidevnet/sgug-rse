%global srcname iptables

%{?filter_setup:
%filter_provides_in %{python_sitearch}/libxtwrapper.so
%filter_setup
}

Name:       python-%{srcname}
Summary:    Python library for manipulating iptables
Version:    0.12.0
Release:    11%{?dist}
License:    ASL 2.0
URL:        https://github.com/ldx/%{name}
Source0:    %{url}/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc

BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
python-iptables is a library for doing iptables manipulations from python.


%package -n python3-%{srcname}
Summary:  %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
python-iptables is a library for doing iptables manipulations from Python 3.


%prep
%setup -q

%build
chmod -x README.md
%py3_build

%install
%py3_install


%files -n python3-%{srcname}
%doc README.md MANIFEST.in
%license NOTICE
%{python3_sitearch}/iptc
%{python3_sitearch}/libxtwrapper*.so
%{python3_sitearch}/python_%{srcname}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 10 2018 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-5
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 20 2017 Chris Lalancette <clalancette@gmail.com> - 0.12.0-1
- Update to upstream 0.12.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.11.0-4
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.11.0-2
- Rebuild for Python 3.6

* Thu Aug 18 2016 Dominika Krejci <dkrejci@redhat.com> - 0.11.0-1
- Add Python 3
- Update to 0.11.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-13
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Dec 14 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.1.0-8
- Simplify installing docs, own package doc dir.

* Mon Aug 12 2013 Chris Lalancette <clalancette@gmail.com> - 0.1.0-7
- Rebuild to remove version from docdir

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 03 2011 Chris Lalancette <clalance@redhat.com> - 0.1.0-2
- Add the license file as doc

* Wed Jul 27 2011 Chris Lalancette <clalance@redhat.com> - 0.1.0-1
- Initial build.
