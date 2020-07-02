%global srcname libnacl

Name:           python-%{srcname}
Version:        1.7.1
Release:        3%{?dist}
Summary:        Python bindings for libsodium based on ctypes

License:        ASL 2.0
URL:            https://libnacl.readthedocs.org/
Source0:        %{pypi_source}

# Remove encoding parameter json.loads for Python 3.9 compatibility.
# Merged upstream: https://github.com/saltstack/libnacl/pull/121
Patch121:       pr121.patch

BuildArch:      noarch
BuildRequires:  libsodium

%description
python-libnacl is used to gain direct access to the functions exposed by
Daniel J. Bernstein’s nacl library via libsodium. It has been constructed
to maintain extensive documentation on how to use nacl as well as being
completely portable.


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
Requires:       libsodium
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
python-libnacl is used to gain direct access to the functions exposed by
Daniel J. Bernstein’s nacl library via libsodium. It has been constructed
to maintain extensive documentation on how to use nacl as well as being
completely portable.


%prep
%autosetup -p1 -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%check
#{__python3} setup.py test
%{__python3} -m unittest discover --start-directory tests -v

%files -n python3-%{srcname}
%license LICENSE
%doc AUTHORS
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Wed Apr 01 2020 Petr Viktorin <pviktori@redhat.com> - 1.7.1-3
- Remove encoding parameter json.loads for Python 3.9 compatibility

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Jonny Heggheim <hegjon@gmail.com> - 1.7.1-1
- Update to 1.7.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 Sérgio Basto <sergio@serjux.com> - 1.6.1-7
- Actually run unit tests

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Jonny Heggheim <hegjon@gmail.com> - 1.6.1-5
- Removed Python 2 sub-package
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 01 2017 Sérgio Basto <sergio@serjux.com> - 1.6.1-1
- Update to 1.6.1

* Thu Oct 05 2017 Sérgio Basto <sergio@serjux.com> - 1.6.0-1
- Update python-libnacl to 1.6.0
- Fix FTBFS with new libsodium

* Mon Oct 02 2017 Remi Collet <remi@fedoraproject.org> - 1.5.2-3
- rebuild for libsodium

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 1.5.2-1
- Update to 1.5.2 (#1463028)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Jonny Heggheim <jonnyheggheim@sigaint.org> - 1.5.0-1
- inital package
