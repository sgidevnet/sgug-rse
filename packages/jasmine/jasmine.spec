%{?nodejs_find_provides_and_requires}

Name:       jasmine
Version:    1.3.1
Release:    13%{?dist}
Summary:    A Behavior-Driven Development (BDD) testing framework for JavaScript
License:    MIT
URL:        http://pivotal.github.com/jasmine/
Source0:    https://github.com/downloads/pivotal/jasmine/jasmine-standalone-%{version}.zip
BuildArch:  noarch

# Take out the version from the library path.
Patch0:     %{name}-1.3.1-lib-location.patch

%description
Jasmine is a Behavior-Driven Development (BDD) testing framework for
JavaScript. It does not rely on browsers, DOM, or any JavaScript framework.
Thus it's suited for websites, Node.js projects, or anywhere that
JavaScript can run.


%prep
%setup -q -c %{name}-%{version}
%patch0 -p1


%build
#nothing to do


%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr lib/jasmine-%{version}/*.css lib/jasmine-%{version}/*.js \
    %{buildroot}%{_datadir}/%{name}


%files
%doc lib/jasmine-%{version}/MIT.LICENSE
%doc spec/ SpecRunner.html src/
%{_datadir}/%{name}


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.3.1-3
- remove unneeded directory

* Sun Mar 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.3.1-2
- move some files from %%{_datadir} to %%doc

* Sun Mar 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.3.1-1
- initial package
