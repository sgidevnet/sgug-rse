Name:		pari-galpol
Version:	20180625
Release:	4%{?dist}
Summary:	PARI/GP Computer Algebra System Galois polynomials
License:	GPLv2+
URL:		http://pari.math.u-bordeaux.fr/packages.html
Source0:	http://pari.math.u-bordeaux.fr/pub/pari/packages/galpol.tgz
Source1:	http://pari.math.u-bordeaux.fr/pub/pari/packages/galpol.tgz.asc
# Public key 0x4522e387, Bill Allombert <Bill.Allombert@math.u-bordeaux.fr>
Source2:	gpgkey-42028EA404A2E9D80AC453148F0E7C2B4522E387.gpg
BuildArch:	noarch

BuildRequires:	gnupg2

%description
This package contains the optional PARI package galpol, which contains a
database of polynomials defining Galois extensions of the rationals
representing all abstract groups of order up to 143 for all signatures
(3657 groups, 7194 polynomials).

%prep
%setup -cq
mv data/galpol/README .

# Verify the source file
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{_datadir}/pari/
cp -a data/galpol %{buildroot}%{_datadir}/pari/
%{_fixperms} %{buildroot}%{_datadir}/pari/

%files
%doc README
%{_datadir}/pari/

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180625-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Jerry James <loganjerry@gmail.com> - 20180625-3
- Verify PGP signatures on the source file

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180625-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 20180625-1
- Update to upstream release from June 25th 2018

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20150915-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20150915-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150915-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150915-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb  5 2016 Paul Howarth <paul@city-fan.org> - 20150915-1
- Update to upstream release from September 15th 2015

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20140218-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140218-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140218-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 24 2014 Paul Howarth <paul@city-fan.org> - 20140218-1
- Initial RPM package
