Name:		python-ansi
Version:	0.1.3
Release:	21%{?dist}
Summary:	ANSI cursor movement and graphics

License:	MIT
URL:		https://github.com/tehmaze/ansi
Source0:	https://pypi.python.org/packages/source/a/ansi/ansi-%{version}.tar.gz

BuildRequires:	python3-devel
BuildArch:	noarch

%global _description\
Various ANSI escape codes, used in moving the cursor in a text console or\
rendering colored text with Python 2.\


%description %_description

%package -n python3-ansi
Summary:	ANSI cursor movement and graphics

%description -n python3-ansi
Various ANSI escape codes, used in moving the cursor in a text console or
rendering colored text with Python 3.

%prep
%setup -qc
mv ansi-%{version} python2
pushd python2
cp -pr README.md LICENSE.md ../
popd

cp -a python2 python3

%build
pushd python2
popd
pushd python3
%{__python3} setup.py build
popd

%install
pushd python2
popd
pushd python3
%{__python3} setup.py install --skip-build --root %{buildroot}
popd

%files -n python3-ansi
%license LICENSE.md
%doc README.md
%{python3_sitelib}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.3-21
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.3-19
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.3-18
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1.3-15
- Subpackage python2-ansi has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Jul 17 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.3-14
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.3-12
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1.3-10
- Python 2 binary package renamed to python2-ansi
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.3-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Jul 27 2015 Sebastian Dyroff <sdyroff@fedoraproject.org> 0.1.3-3
- Improve source url (BZ #1245356)
- Remove CFLAGS (BZ #1245356)
- Fix changelog (BZ #1245356)

* Wed Jul 08 2015 Sebasitan Dyroff <sdyroff@fedoraproject.org> 0.1.3-2
- Fix source url (BZ #1245356)

* Tue Jul 07 2015 Sebasitan Dyroff <sdyroff@fedoraproject.org> 0.1.3-1
- Initial packaging
