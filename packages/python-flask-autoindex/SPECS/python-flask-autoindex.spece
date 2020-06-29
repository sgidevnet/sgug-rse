%{?python_enable_dependency_generator}
%global mod_name	Flask-AutoIndex

Name:		python-flask-autoindex
Version:	0.6.6
Release:	2%{?dist}
Summary:	A mod_autoindex for Flask
License:	BSD
URL:		https://github.com/general03/flask-autoindex
Source0:	%{url}/archive/v%{version}/%{mod_name}-%{version}.tar.gz
BuildArch:	noarch

%global _description\
Flask-AutoIndex generates an index page for your Flask application\
automatically. The result is just like mod_autoindex, but the look is\
more awesome!

%description %_description

%package -n python3-flask-autoindex
Summary: %summary
BuildRequires:	python3-devel
BuildRequires:	python3-flask
BuildRequires:	python3-flask-silk
BuildRequires:	python3-future
BuildRequires:	python3-setuptools
BuildRequires:	python3-sphinx
Conflicts:	python2-flask-autoindex < 0.6-4

%description -n python3-flask-autoindex %_description

%package docs
Summary:	Documentation for %{name}

%description docs
HTML documentation for %{name}.

%prep
%autosetup -n flask-autoindex-%{version}

# Fix the sphinx config
sed -i "s/^extension.*/& 'sphinx.ext.autodoc'/" docs/conf.py

%build
%py3_build

# Build the documentation
PYTHONPATH=$PWD/build/lib sphinx-build docs html

%install
%py3_install


%check
python3 setup.py test

%files -n python3-flask-autoindex
%doc CHANGELOG.md README.md
%license LICENSE.md
%{_bindir}/fai
%{python3_sitelib}/flask_autoindex/
%{python3_sitelib}/*.egg-info/

%files docs
%doc html/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.6-2
- Rebuilt for Python 3.9

* Tue May 19 2020 Jerry James <loganjerry@gmail.com> - 0.6.6-1
- Version 0.6.6
- Update URLs

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6-5
- Enable python dependency generator

* Fri Jan 04 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6-4
- Subpackage python2-flask-autoindex has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6-2
- Rebuilt for Python 3.7

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 0.6-1
- Update to latest upstream release
- Use license macro
- Build for both python 2 and python 3
- Build documentation

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.1-16
- Python 2 binary package renamed to python2-flask-autoindex
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-13
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 11 2013 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.4.1-9
- Correct rawhide FTBFS (#992891)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 19 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.4.1-6
- Update to match upstream new tarball but with same version
  The new tarball was done to address issues in the review process
- Add %%check section to use new test files in upstream tarball
- Remove LICENSE Source1 as it is now in upstream tarball

* Tue Sep 18 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.4.1-5
- Correct incoherent version in changelog
- Add LICENSE file from upstream to source rpm

* Thu Sep 13 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.4.1-4
- Add missing python-setuptools build requires (#839071)

* Fri Aug 17 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.4.1-3
- Correct package for clean mock chroot build

* Sun Aug 5 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.4.1-2
- No need to set CFLAGS for noarch (#839071)
- Add requires of python-flask-silk (#839097)

* Tue Jul 10 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.4.1-1
- Initial python-flask-autoindex spec.
