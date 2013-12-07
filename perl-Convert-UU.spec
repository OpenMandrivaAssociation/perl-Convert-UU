%define modname	Convert-UU
%define modver	0.5201

Summary:	UUencode and UUdecode
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	7
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Convert/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
* * uuencode

  uuencode() takes as the first argument a string that is to be uuencoded.
  Note, that it is the string that is encoded, not a filename.
  Alternatively a filehandle may be passed that must be opened for reading.
  It returns the uuencoded string including 'begin' and 'end'. Second and
  third argument are optional and specify filename and mode. If unspecified
  these default to "uuencode.uu" and 644.

* * uudecode

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc ChangeLog README META.yml
%{perl_vendorlib}/*
%{_bindir}/puudecode
%{_bindir}/puuencode
%{_mandir}/man1/puudecode.1*
%{_mandir}/man1/puuencode.1*
%{_mandir}/man3/*

