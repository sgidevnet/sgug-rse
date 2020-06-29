Name:		python-passlib
Version:	1.7.2
Release:	2%{?dist}
Summary:	Comprehensive password hashing framework supporting over 20 schemes

License:	BSD and Beerware and Copyright only
URL:		https://bitbucket.org/ecollins/passlib
Source0:	https://pypi.io/packages/source/p/passlib/passlib-%{version}.tar.gz

Patch0:     passlib-1.7.2-py39-crypt.patch

BuildArch:	noarch

# docs generation requires python-cloud-sptheme, which isn't packaged yet.
# so we won't generate the docs yet.
#BuildRequires:	python2-sphinx >= 1.0
#BuildRequires:	python2-cloud-sptheme

%description
Passlib is a password hashing library for Python 2 & 3, which provides
cross-platform implementations of over 20 password hashing algorithms,
as well as a framework for managing existing password hashes. It's
designed to be useful for a wide range of tasks, from verifying a hash
found in /etc/shadow, to providing full-strength password hashing for
multi-user application.


%package -n python3-passlib
Summary:	Comprehensive password hashing framework supporting over 20 schemes
%{?python_provide:%python_provide python3-passlib}

BuildRequires:	python3-devel
BuildRequires:	python3-nose
BuildRequires:	python3-setuptools

%description -n python3-passlib
Passlib is a password hashing library for Python 2 & 3, which provides
cross-platform implementations of over 20 password hashing algorithms,
as well as a framework for managing existing password hashes. It's
designed to be useful for a wide range of tasks, from verifying a hash
found in /etc/shadow, to providing full-strength password hashing for
multi-user application.


%prep
%autosetup -n passlib-%{version} -p 1
rm -fr *.egg*


%build
%py3_build


%install
# passlib setup.py append HG revision to the end of version by default
# which makes StrictVersion checks complaining
export PASSLIB_SETUP_TAG_RELEASE="no"
%py3_install


%check
nosetests-%{python3_version} -v


%files -n python3-passlib
%doc README
%license LICENSE
%{python3_sitelib}/passlib*/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.2-2
- Rebuilt for Python 3.9

* Wed Feb 26 2020 Alan Pevec <alan.pevec@redhat.com> 1.7.2-1
- Update to 1.7.2
- py39 crypt change https://bitbucket.org/ecollins/passlib/issues/115

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.1-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.1-3
- Subpackage python2-passlib has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Wed Mar 13 2019 Björn Esser <besser82@fedoraproject.org> - 1.7.1-2
- Use new python macros
- Add conditional to turn off python2 packages
- Remove egg(-info) before build
- Run testsuite

* Wed Feb 06 2019 Björn Esser <besser82@fedoraproject.org> - 1.7.1-1
- Update to 1.7.1 (#1620382)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-9
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.7.0-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 04 2018 Troy Dawson <tdawson@redhat.com> - 1.7.0-6
- Update conditional

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 23 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 1.7.0-4
- Fix eggs-info generation

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-2
- Rebuild for Python 3.6

* Wed Nov 30 2016 Alan Pevec <alan.pevec@redhat.com> 1.7.0-1
- Update to 1.7.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Sep 07 2015 Chandan Kumar <chkumar246@gmail.com> - 1.6.5-1
- Added python2 and python3 subpackage
- updated to 1.6.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 19 2014 Alan Pevec <apevec@redhat.com> - 1.6.2-1
- update to 1.6.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 04 2013 Alan Pevec <apevec@redhat.com> - 1.6.1-1
- update to 1.6.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Matt Domsch <Matt_Domsch@dell.com> - 1.5.3-1
- initial release for Fedora
