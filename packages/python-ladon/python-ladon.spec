Name:           python-ladon
Version:        0.9.38
Release:        9%{?dist}
Summary:        Multiprotocol approach to creating a webservice

License:        LGPLv3+
URL:            http://ladonize.org
Source0:        http://pypi.python.org/packages/source/l/ladon/ladon-%{version}.tar.gz
Source1:        http://bazaar.launchpad.net/~ladon-dev-team/ladon/ladon/download/head:/license.txt-20110711093707-sf2ym6bw134bxkep-7/LICENSE.txt

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-nose
BuildRequires:  python3-chardet
Requires:       python3-jinja2
Requires:       python3-chardet
Provides:       python3-ladon

%description
Ladon is a framework for exposing methods to several internet service 
protocols. Once a method is ladonized it is automatically served through 
all the interfaces that your ladon installation contains. Ladon's interface 
implementations are added in a modular fashion making it very easy extend 
Ladon's protocol support. 

%prep
%setup -q -n ladon-%{version}

# remove egg-info:
rm -rf src/ladon.egg-info

# remove bundled chardet lib
rm -rf src/chardet_py2
rm -rf src/chardet_py3

# remove reference to sphinx-bootstrap-theme
sed -i -e "s/,'sphinx_bootstrap_theme'//" setup.py

# correct references to chardet
for i in `find src/ladon -name '*.py'`; do
    sed -i -e 's/chardet_py2/chardet/' $i
    sed -i -e 's/chardet_py3/chardet/' $i
done

# Fix shebang to avoid auto-generating Python 2 dependency.
sed -i '1s=^#!/usr/bin/python=#!%{__python3}=' src/ladon/clients/jsonwsp.py


%build
%{__python3} setup.py build


%install
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
chmod 755 %{buildroot}/%{python3_sitelib}/ladon/clients/jsonwsp.py
# Remove script and make symlink.
rm %{buildroot}/%{_bindir}/ladon-ctl
ln -s ./ladon-%{python3_version}-ctl %{buildroot}/%{_bindir}/ladon-ctl

cp -p %{SOURCE1} LICENSE

%check
%{__python3} setup.py test
%{__python3} setup.py nosetests


%files
%doc PKG-INFO README.rst examples
%license LICENSE
%{python3_sitelib}/ladon
%{python3_sitelib}/ladon-%{version}-py?.?.egg-info
%{_bindir}/ladon-%{python3_version}-ctl
%{_bindir}/ladon-ctl

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.38-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.38-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.38-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.38-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.38-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.38-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 28 2017 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.38-3
- Fix auto-generating Python 2 dependency

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 CAI Qian <caiqian@redhat.com> - 0.9.38-1
- update to 0.9.38 (rhbz#1219035)
- update to use python3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.24-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb 19 2015 Matthias Runge <mrunge@redhat.com> - 0.9.24-1
- update to 0.9.24 (rhbz#1050917)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 02 2014 Matthias Runge <mrunge@redhat.com> - 0.8.8-1
- update to 0.8.8 (rhbz#1007324)

* Fri Jul 26 2013 Matthias Runge <mrunge@redhat.com> - 0.8.2-1
- update to 0.8.2 (rhbz#984618)

* Tue May 28 2013 Matthias Runge <mrunge@redhat.com> - 0.8.1-1
- update to 0.8.1 (rhbz#859948)

* Thu Apr 25 2013 Matthias Runge <mrunge@redhat.com> - 0.7.9-1
- update to 0.7.9 (rhbz#956017)

* Mon Mar 25 2013 Matthias Runge <mrunge@redhat.com> - 0.7.8-1
- update to 0.7.8 (rhbz#924739)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 18 2012 Matthias Runge <mrunge@redhat.com> - 0.7.5-1
- update to latest upstream release 0.7.5

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 23 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.7.0-2
- bump version to maintain fedora upgrade-ability

* Mon Mar 12 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.7.0-1
- update to version 0.7.0
- spec cleanup
- make sure, removed bundled lib isn't referenced anymore

* Thu Feb 02 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.6.7-1
- update to Version 0.6.7

* Fri Jan 06 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.6.5-2
- remove unecessary definition, buildroot cleaning
- correct build requirements

* Wed Jan 04 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.6.5-1
- initial fedora package
