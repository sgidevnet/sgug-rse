%bcond_without gdbm
%bcond_with sqlite
%bcond_with mysql

Name:           qsf
Version:        1.2.11
Release:        9%{?dist}
Summary:        Quick Spam Filter

License:        Artistic 2.0
URL:            http://www.ivarch.com/programs/qsf/
Source0:        http://downloads.sourceforge.net/qsf/qsf-%{version}.tar.bz2

BuildRequires:  gcc

%{?with_gdbm:BuildRequires: gdbm-devel}
%{?with_sqlite:BuildRequires: sqlite2-devel}
%{?with_mysql:BuildRequires: mariadb-connector-c-devel}

%description
Quick Spam Filter (QSF) is an Open Source email classification filter,
designed to be small, fast, and accurate, which works to classify
incoming email as either spam or non-spam.

To recognise spam, QSF strips the text out of the email (using MIME
decoding and HTML stripping) and then splits it into tokens (words,
word pairs, URLs, and so on). These tokens are then looked up in a
database and analysed using the Bayesian technique to see whether the
email should be classified as spam or not.

QSF is designed to be run by an MDA, such as procmail.

%prep
%setup -q

%build
%configure \
%{!?with_gdbm:    --without-gdbm} \
%{!?with_sqlite:  --without-sqlite} \
%{!?with_mysql:   --without-mysql} \
;
make %{?_smp_mflags}

%check
make test

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc README doc/COPYING doc/NEWS doc/TODO doc/postfix-howto
%{_bindir}/qsf
%{_mandir}/man1/qsf.1*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Miroslav Lichvar <mlichvar@redhat.com> 1.2.11-7
- add gcc to build requirements

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Miroslav Lichvar <mlichvar@redhat.com> 1.2.11-4
- rebuild with new gdbm

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 26 2017 Miroslav Lichvar <mlichvar@redhat.com> 1.2.11-1
- update to 1.2.11
- remove obsolete macros

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Mar 17 2010 Miroslav Lichvar <mlichvar@redhat.com> 1.2.7-5
- rebuild with new gdbm
- use bcond macros

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.7-2
- Autorebuild for GCC 4.3

* Tue Aug 28 2007 Miroslav Lichvar <mlichvar@redhat.com> 1.2.7-1
- update to 1.2.7

* Fri May 04 2007 Miroslav Lichvar <mlichvar@redhat.com> 1.2.6-2
- add %%check (#238691)

* Wed May 02 2007 Miroslav Lichvar <mlichvar@redhat.com> 1.2.6-1
- initial release
